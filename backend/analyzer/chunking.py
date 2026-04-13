###############################################################################################
#### CHUNKING : módulo encargado de la división de textos de las fuentes proporcionadas
###############################################################################################

def dividir_codigo(texto, max_chars=1500):
    chunks = []

    for i in range(0, len(texto), max_chars):
        chunk = texto[i:i + max_chars]

        chunks.append({
            "chunk": chunk,
            "start": i,
            "end": i + max_chars
        })

    return chunks