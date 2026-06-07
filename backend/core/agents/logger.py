import logging
from datetime import datetime
import os

# funcion para guardar las metricas obtenidas del analisis en un log
def logging_metricas(nombre_metricas: str, ruta: str, metricas: dict, logs_dir="logs"):

    # asegurar directorio
    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        logs_dir,
        f"metricas_{nombre_metricas}_{timestamp}.log"
    )

    logger = logging.getLogger(f"metricas_{nombre_metricas}")

    # evitar duplicar handlers si se llama varias veces
    if not logger.handlers:

        logger.setLevel(logging.INFO)

        handler = logging.FileHandler(
            filename,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info("=== MÉTRICAS %s ===", nombre_metricas.upper())
    logger.info("-> RUTA ANALIZADA: %s ", ruta)

    for nombre, valor in metricas.items():
        logger.info("%s: %s", nombre, valor)

    return filename