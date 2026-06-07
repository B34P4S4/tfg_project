# METRICAS QUE VALORAN LA DETECCION DE VULNERABILIDADES
from sklearn.metrics import cohen_kappa_score

# --------------------------------------------------------------------------------------
# Porcentaje de vulnerabilidades en las que ambos modelos coinciden: Agreement Rate
def get_ratio_acuerdo(model_a: set, model_b: set) -> float:
    union = model_a | model_b

    if not union:
        return 1.0

    intersection = model_a & model_b

    return len(intersection) / len(union)

# --------------------------------------------------------------------------------------
# Porcentaje de vulnerabilidades en las que los modelos difieren: Disagreement Rate
def get_ratio_desacuerdo(model_a: set, model_b: set) -> float:

    union = model_a | model_b

    if not union:
        return 0.0

    disagreements = union - (model_a & model_b)

    return len(disagreements) / len(union)

# --------------------------------------------------------------------------------------
# Porcentaje de concordancia entre modelos: Cohen's Kappa
    # <0	peor que azar
    # 0-0.2	leve
    # 0.2-0.4	aceptable
    # 0.4-0.6	moderada
    # 0.6-0.8	sustancial
    # >0.8	casi perfecta
def get_cohen_kappa(
    openai_vulns: set,
    gemini_vulns: set,
    all_vulnerabilities: set
) -> float:

    openai_binary = [
        1 if v in openai_vulns else 0
        for v in all_vulnerabilities
    ]

    gemini_binary = [
        1 if v in gemini_vulns else 0
        for v in all_vulnerabilities
    ]

    return cohen_kappa_score(
        openai_binary,
        gemini_binary
    )

# --------------------------------------------------------------------------------------
# Mejora obtenida al combinar ambos modelos respecto a usar uno individual: Ensembre Gain
def get_ensemble_gain(
    recall_openai: float,
    recall_gemini: float,
    recall_ensemble: float
) -> float:

    best_single = max(
        recall_openai,
        recall_gemini
    )

    if best_single == 0:
        return None

    return (
        (recall_ensemble - best_single)
        / best_single
    ) * 100

# --------------------------------------------------------------------------------------
# Porcentaje de las vulnerabilidades reales has conseguido detectar
def get_recall(detected: set, ground_truth: set) -> float:

    if not ground_truth:
        return 1.0

    tp = len(detected & ground_truth)

    return tp / len(ground_truth)

# --------------------------------------------------------------------------------------
# Porcentaje de vulnerabilidades críticas reales detectadas: Critical Vulnerability Recall
def get_critical_vulnerability_recall(
    detected: set,
    critical_ground_truth: set
) -> float:

    if not critical_ground_truth:
        return 1.0

    true_positives = len(
        detected & critical_ground_truth
    )

    return (
        true_positives
        / len(critical_ground_truth)
    )

# --------------------------------------------------------------------------------------
# Obtiene una combinacion de campos de cada vulnerabilidad detectada para identificarla univocante
def get_vulnerabilidad_id(item):

    return (
        item["file"],
        item["chunk_id"],
        item["cwe"]
    )

# --------------------------------------------------------------------------------------
# Obtiene el número de vulnerabilidades detectadas por modelo de IA
def get_detectadas_por_modelo(data,model_name):

    return {
        get_vulnerabilidad_id(item)
        for item in data
        if item["modelo"] == model_name
    }

# --------------------------------------------------------------------------------------
# Obtiene el nivel de fiabilidad en la detección de vulnerabilidades del modelo IA segun porcentaje de exactitud
def get_ground_truth(
    data,
    min_accuracy=80 # minimo de exactitud requerido para no considerarse una alucinación del modelo IA, obteniendose comparando con RAG (base de conocimiento contrastada)
):

    return {
        get_vulnerabilidad_id(item)
        for item in data
        if item["accuracy_score"] >= min_accuracy
    }

# --------------------------------------------------------------------------------------
# Obtiene el nivel de fiabilidad en la detección de vulnerabilidades del modelo IA segun porcentaje de exactitud y numero de vulnerabilidades detectadas
def get_critical_ground_truth(
    data,
    min_accuracy=80, # minimo de exactitud requerido para no considerarse una alucinación del modelo IA, obteniendose comparando con RAG (base de conocimiento contrastada)
    min_cvss=9 # minimo número de vulnerabilidades detectadas para considerar el analisis fiable
):

    return {
        get_vulnerabilidad_id(item)
        for item in data
        if (
            item["accuracy_score"] >= min_accuracy
            and item["cvss"] >= min_cvss
        )
    }

# --------------------------------------------------------------------------------------
# Obtenemos todas las vulnerabilidades detectadas
def get_all_findings(data):

    return {
        get_vulnerabilidad_id(item)
        for item in data
    }

# --------------------------------------------------------------------------------------
# FUNCION PARA LLAMAR A TODAS LAS DEMAS
# Calcula todas las métricas de evaluación de detección de vulnerabilidades
def get_metricas_deteccion_vulns(data):

    detectadas_openai = (
        get_detectadas_por_modelo(
            data,
            "OpenAI"
        )
    )

    detectadas_gemini = (
        get_detectadas_por_modelo(
            data,
            "Gemini"
        )
    )

    ground_truth = (
        get_ground_truth(data)
    )

    critical_ground_truth = (
        get_critical_ground_truth(data)
    )

    detectadas_todas = (
        get_all_findings(data)
    )

    detectadas_union = (
        detectadas_openai |
        detectadas_gemini
    )

    acuerdo = get_ratio_acuerdo(
        detectadas_openai,
        detectadas_gemini
    )

    desacuerdo = get_ratio_desacuerdo(
        detectadas_openai,
        detectadas_gemini
    )

    kappa = get_cohen_kappa(
        detectadas_openai,
        detectadas_gemini,
        detectadas_todas
    )

    recall_openai = get_recall(
        detectadas_openai,
        ground_truth
    )

    recall_gemini = get_recall(
        detectadas_gemini,
        ground_truth
    )

    recall_ensemble = get_recall(
        detectadas_union,
        ground_truth
    )

    gain = get_ensemble_gain(
        recall_openai,
        recall_gemini,
        recall_ensemble
    )

    critical_recall = (
        get_critical_vulnerability_recall(
            detectadas_union,
            critical_ground_truth
        )
    )

    return {
        "Ratio de acuerdo entre modelos (%)":
            round(acuerdo * 100, 2),
            
        "Ratio de desacuerdo entre modelos (%)":
            round(desacuerdo * 100, 2),

        "Cohen's Kappa":
            round(kappa, 4),

        "Recall OpenAI (%)":
            round(recall_openai * 100, 2),

        "Recall Gemini (%)":
            round(recall_gemini * 100, 2),

        "Recall Ensemble (%)":
            round(recall_ensemble * 100, 2),

        "Ensemble Gain (%)":
            round(gain, 2),

        "Critical Vulnerability Recall (%)":
            round(critical_recall * 100, 2)
    }