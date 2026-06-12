# METRICAS DE COMPARACION ENTRE MODELOS, LENGUAJE A ANALIZAR Y PIPELINES
from backend.testing.metrics_testing.vul_detection_testing import get_precision,get_recall,get_falsos_negativos,get_falsos_positivos,get_detectadas_por_modelo
from backend.testing.metrics_testing.rag_testing import get_aceptado_rag

def get_compara_modeloIA(data):

    ground_truth = get_ground_truth_rag(data)

    resultados = {}

    for modelo in ["OpenAI", "Gemini"]:

        detected = get_detectadas_por_modelo(
            data,
            modelo
        )

        precision = get_precision(
            detected,
            ground_truth
        )

        recall = get_recall(
            detected,
            ground_truth
        )

        fp = get_falsos_positivos(
            detected,
            ground_truth
        )

        fn = get_falsos_negativos(
            detected,
            ground_truth
        )

        resultados[modelo] = {

            "Precision (%)":
                round(precision * 100, 2),

            "Recall (%)":
                round(recall * 100, 2),

            "Falsos Positivos (%)":
                round(fp * 100, 2),

            "Falsos Negativos (%)":
                round(fn * 100, 2)
        }

    return resultados

def get_compara_lenguaje(data):

    resultados = {}

    ground_truth = get_ground_truth_rag(data)

    languages = {

        item["language"]

        for item in data
    }

    for language in languages:

        detected = {

            (
                x["file"],
                x["chunk_id"],
                x["cwe"]
            )

            for x in data

            if x["language"] == language
        }

        precision = get_precision(
            detected,
            ground_truth
        )

        recall = get_recall(
            detected,
            ground_truth
        )

        resultados[language] = {

            "Precision (%)":
                round(precision * 100, 2),

            "Recall (%)":
                round(recall * 100, 2)
        }

    return resultados

def get_compara_pipelines(
    pipelines,
    ground_truth
):

    resultados = {}

    for (
        nombre_pipeline,
        detected
    ) in pipelines.items():

        precision = get_precision(
            detected,
            ground_truth
        )

        recall = get_recall(
            detected,
            ground_truth
        )

        fp = get_falsos_positivos(
            detected,
            ground_truth
        )

        fn = get_falsos_negativos(
            detected,
            ground_truth
        )

        resultados[nombre_pipeline] = {

            "Precision (%)":
                round(
                    precision * 100,
                    2
                ),

            "Recall (%)":
                round(
                    recall * 100,
                    2
                ),            

            "Falsos Positivos (%)":
                round(
                    fp * 100,
                    2
                ),

            "Falsos Negativos (%)":
                round(
                    fn * 100,
                    2
                )
        }

    return resultados

def get_metricas_pipelines(data):

    ground_truth = get_ground_truth_rag(data)

    openai = get_detectadas_por_modelo(
        data,
        "OpenAI"
    )

    gemini = get_detectadas_por_modelo(
        data,
        "Gemini"
    )

    ensemble = (
        openai |
        gemini
    )

    pipelines = {

        "OpenAI":
            openai,

        "Gemini":
            gemini,

        "Union de modelos":
            ensemble
    }

    return get_compara_pipelines(
        pipelines,
        ground_truth
    )

def get_ground_truth_rag(
    data,
    threshold=80
):

    accepted = get_aceptado_rag(
        data,
        threshold
    )

    return {

        (
            item["file"],
            item["chunk_id"],
            item["cwe"]
        )

        for item in accepted
    }

def get_metricas_comparativa(data):

    return {

        "Por lenguaje":
            get_compara_lenguaje(data),

        "Por modelo":
            get_compara_modeloIA(data),

        "Por pipeline":
            get_metricas_pipelines(data)
    }
