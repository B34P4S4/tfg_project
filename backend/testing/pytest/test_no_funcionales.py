# PRUEBAS NO FUNCIONALES CON PYTEST

def test_tiempo(resultado_analisis):

    tiempo = resultado_analisis[
        "metricas_rendimiento"
    ]["tiempo_total_segundos"]

    assert tiempo < 600


def test_memoria(resultado_analisis):

    memoria = resultado_analisis[
        "metricas_rendimiento"
    ]["memoria_consumida_mb"]

    assert memoria < 100


def test_tiempo_por_archivo(resultado_analisis):

    tiempo = resultado_analisis[
        "metricas_rendimiento"
    ]["tiempo_medio_archivo"]

    assert tiempo < 30