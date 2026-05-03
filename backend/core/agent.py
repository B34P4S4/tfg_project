from .mock_llm import analizar_codigo_mock

def analizar_archivo(file_data):
    resultados = []

    for chunk in file_data["chunks"]:
        vulns = analizar_codigo_mock(chunk["chunk"])

        for v in vulns:
            resultados.append({
                "file": file_data["file"],
                "chunk_start": chunk["start"],
                "chunk_end": chunk["end"],
                **v
            })

    return resultados


def analizar_proyecto(proyecto):
    resultado_final = []

    for archivo in proyecto:
        resultado_final.extend(analizar_archivo(archivo))

    return resultado_final