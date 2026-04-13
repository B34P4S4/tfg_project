###############################################################################################
#### PROCESSOR : módulo encargado del acceso a los archivos que se han de analizar
###############################################################################################

import os
from .chunking import dividir_codigo

# EXTENSIONES DE ARCHIVOS ANALIZABLES POR LA APLICACIÓN
EXTENSIONES_VALIDAS = [".py", ".js", ".tsx", ".php", ".sql"]

###
# Accede a la ruta indicada para obtener los archivos del proyecto a analizar
###
def leer_proyecto(ruta):
    archivos = []

    for root, _, files in os.walk(ruta):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONES_VALIDAS):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read()

                archivos.append({
                    "file": path,
                    "content": contenido
                })

    return archivos

###
# Divide el contenido de los archivos en la ruta indicada
###
def procesar_proyecto(ruta):
    archivos = leer_proyecto(ruta)

    resultado = []

    for archivo in archivos:
        chunks = dividir_codigo(archivo["content"])

        resultado.append({
            "file": archivo["file"],
            "chunks": chunks
        })

    return resultado