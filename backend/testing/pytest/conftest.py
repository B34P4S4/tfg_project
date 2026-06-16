import pytest
from backend.core.agents.agent import analizar_proyecto

# SE IRA CAMBIANDO SEGUN EL CORPUS QUE SE APLIQUE PARA LAS PRUEBAS
RUTA_TEST = (
    "backend/testing/corpus/python"
)

@pytest.fixture(scope="session")
def resultado_analisis():
    # Ejecuta TODO el pipeline una sola vez y lo reutiliza en todos los tests.
    print("\n[FIXTURE] Ejecutando analisis completo una única vez...")
    resultado = analizar_proyecto(RUTA_TEST)
    return resultado