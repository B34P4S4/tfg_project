# PRUEBAS FUNCIONALES CON PYTEST

def test_recall_ensemble(resultado_analisis):

    recall = resultado_analisis[
        "metricas_vulnerabilidades"
    ]["Recall Ensemble (%)"]

    assert recall >= 90


def test_critical_recall(resultado_analisis):

    recall = resultado_analisis[
        "metricas_vulnerabilidades"
    ][
        "Critical Vulnerability Recall (%)"
    ]

    assert recall == 100


def test_rag(resultado_analisis):

    assert resultado_analisis[
        "metricas_rag"
    ]["Ratio de aceptación de RAG (%)"] > 80


def test_cobertura_ataques(resultado_analisis):

    cobertura = resultado_analisis[
        "metricas_ataques"
    ]["Cobertura de ataque (%)"]

    assert cobertura > 30

def test_precision(resultado_analisis):

    precision = resultado_analisis[
        "metricas_vulnerabilidades"
    ][
        "Precisión (%)"
    ]

    assert precision >= 80

# AUNQUE YA OBTENEMOS RECALL Y PRECISION HACEMOS UN TESTING ESPECÍFICO DE F.POSITIVOS Y F.NEGATIVOS
# Precisión alta >> pocos falsos positivos
# Recall alto >> pocos falsos negativos

def test_falsos_positivos(resultado_analisis):

    fp = resultado_analisis[
        "metricas_vulnerabilidades"
    ]["Falsos positivos (%)"]

    assert fp <= 20

def test_falsos_negativos(resultado_analisis):

    fn = resultado_analisis[
        "metricas_vulnerabilidades"
    ]["Falsos negativos (%)"]

    assert fn <= 5

