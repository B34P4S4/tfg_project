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

def dividir_codigo_lineas(code, max_lines=50):
    lines = code.split("\n")
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i:i+max_lines])
        chunks.append(chunk)

    return chunks