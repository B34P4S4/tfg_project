import statistics

# De lo que el modelo detecta, cuánto es válido según RAG si su accuracy_score es mayor igual 80 para filtrar alucinaciones
def get_aceptado_rag(data, threshold=80):

    return [
        item for item in data
        if item["accuracy_score"] >= threshold
    ]

def get_ratio_aceptado_rag(data, threshold=80):

    if not data:
        return 0.0

    accepted = get_aceptado_rag(data, threshold)

    return len(accepted) / len(data)

def get_confianza_media_rag(data):

    scores = [
        item["accuracy_score"]
        for item in data
    ]

    return statistics.mean(scores)

def get_confianza_rag(data):

    scores = [
        item["accuracy_score"]
        for item in data
    ]

    if len(scores) < 2:
        return 0.0

    return statistics.stdev(scores)

def get_ratio_cobertura_rag(data, model):

    filtered = [
        item for item in data
        if item["modelo"] == model
    ]

    if not filtered:
        return 0.0

    accepted = [
        item for item in filtered
        if item["accuracy_score"] >= 80
    ]

    return len(accepted) / len(filtered)

def get_metricas_rag(data, threshold=80):

    accepted = get_aceptado_rag(data, threshold)

    return {
        "Ratio de aceptación de RAG (%)":
            round(len(accepted) / len(data) * 100, 2),

        "Confianza media de RAG":
            round(get_confianza_media_rag(data), 2),

        "Ratio de dispersión en el RAG":
            round(get_confianza_rag(data), 2),
    }