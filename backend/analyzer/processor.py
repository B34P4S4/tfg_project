###############################################################################################
#### PROCESSOR : módulo encargado del acceso a los archivos que se han de analizar
###############################################################################################

import os
from .chunking import dividir_codigo

# EXTENSIONES DE ARCHIVOS ANALIZABLES POR LA APLICACIÓN
EXTENSIONES_VALIDAS = [".py", ".js", ".ts", ".php", ".sql"]

###
# Detecta el lenguaje de programación y devuelve el nombre
###
def detecta_lenguaje(extension):
    lenguaje = "otro"

    match extension:
        case ".py":
            lenguaje = "python"
        case ".js":
            lenguaje = "javascript"
        case ".ts":
            lenguaje = "typescript"
        case ".php":
            lenguaje = "PHP"
        case ".sql":
            lenguaje = "SQL"
        case _:
            lenguaje = "otro"

    return lenguaje


###
# Accede a la ruta indicada para obtener los archivos del proyecto a analizar
###
def leer_proyecto(ruta):
    archivos = []

    for root, _, files in os.walk(ruta):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONES_VALIDAS):
                path = os.path.join(root, file)
                
                # Obtener la extensión del archivo
                _, extension = os.path.splitext(file)

                lenguaje = detecta_lenguaje(extension)

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read()

                archivos.append({
                    "file": path,
                    "extension": extension,
                    "lenguaje": lenguaje,
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
            "extension": archivo["extension"],
            "lenguaje": archivo["lenguaje"],
            "chunks": chunks
        })

    return resultado