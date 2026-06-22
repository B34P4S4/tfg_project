# PRUEBAS FUNCIONALES CON PYTEST

# Mide la capacidad de la combinación de modelos para identificar correctamente 
# todos los casos positivos reales dentro de un conjunto de datos. 
# Para darlo por correcto debe ser igual a mayor al 90%
def test_recall_ensemble(resultado_analisis):

    recall = resultado_analisis[
        "metricas_vulnerabilidades"
    ]["Recall Ensemble (%)"]

    assert recall >= 90

# Mide la capacidad de detección de vulnerabilidades críticas
# Debe ser del 100% para considerarse adecuado
def test_critical_recall(resultado_analisis):

    recall = resultado_analisis[
        "metricas_vulnerabilidades"
    ][
        "Critical Vulnerability Recall (%)"
    ]

    assert recall == 100

# Mide la efectividad del proceso de validación y enriquecimiento mediante RAG
def test_rag(resultado_analisis):

    assert resultado_analisis[
        "metricas_rag"
    ]["Ratio de aceptación de RAG (%)"] > 80

# Mide la capacidad de detectar al menos una proporción mínima de los ataques incluidos en el conjunto de pruebas
def test_cobertura_ataques(resultado_analisis):

    cobertura = resultado_analisis[
        "metricas_ataques"
    ]["Cobertura de ataque (%)"]

    assert cobertura > 30

# Verifica que el porcentaje de vulnerabilidades detectadas correctamente respecto al total de 
# vulnerabilidades reportadas sea igual o superior al 80 %
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

