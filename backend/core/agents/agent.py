import json

from backend.config import MODELO1,MODELO2

from backend.core.processing.repository.processor import procesar_proyecto
from backend.core.processing.vulnerability.processor_vul import modelar_id_vulnerabilidad
from backend.core.processing.vulnerability.correlator_vul import correlacionar,get_correlation_base
from backend.core.agents.prompt_builder import construir_prompt
from backend.core.parsing.parser import parsear_salida_IA
from backend.core.parsing.deduplicator import deduplicar, calcular_accuracy
from backend.storage.repository import guardar_analisis
from backend.storage.statistics_db import get_estadisticas_globales
from backend.testing.db_testing.test_db import test_resultados_bd

from backend.ai.rag.retriever import recuperar_contexto
from backend.ai.rag.init_rag import init_vector_store
from backend.ai.models.client_openAI import analizar_ia1
from backend.ai.models.client_geminiAI import analizar_ia2

from backend.testing.metrics_testing.vul_detection_testing import get_metricas_deteccion_vulns
from backend.testing.metrics_testing.rag_testing import get_metricas_rag
from backend.testing.metrics_testing.attack_detection_testing import get_metricas_ataques
from backend.testing.metrics_testing.comparision_testing import get_metricas_comparativa
from backend.testing.performance_testing.comportamiento_testing import medir_tiempo_total,medir_consumo_memoria
from backend.core.agents.logger import logging_metricas

import time
import os
import psutil

# inicializamos RAG 
vector_store = init_vector_store()
# print("VECTOR STORE agent:", vector_store)

# --------------------------------------------
# PIPELINE PRINCIPAL
# --------------------------------------------

def analizar_proyecto(ruta):
    # --------------------------------------------------
    # ------------ PARA EL ANALISIS NO FUNCIONAL
    # --------------------------------------------------
    inicio_analisis = time.perf_counter()
    proceso = psutil.Process(os.getpid())
    memoria_inicio = proceso.memory_info().rss
    
    proyecto = procesar_proyecto(ruta)
    vulnerabilidades = []

    for archivo in proyecto:

        print("Procesando:", archivo["file"])

        for chunk_id, chunk in enumerate(archivo["chunks"]):

            print(f"Chunk {chunk_id + 1}/"f"{len(archivo['chunks'])}")

            # RAG
            context = recuperar_contexto(chunk,vector_store)
            # PROMPT
            prompt = construir_prompt(context,chunk,file_path=archivo["file"],lenguaje=archivo["lenguaje"])

            
            # OPENAI
            parsed_ia1 = parsear_salida_IA(analizar_ia1(prompt))
            # GEMINI
            parsed_ia2 = parsear_salida_IA(analizar_ia2(prompt))

            # MODELADO DE VULNERABILIDADES
            if parsed_ia1.get("1.1"):

                vuln_ia1 = modelar_id_vulnerabilidad(parsed_ia1,MODELO1, archivo["file"],chunk_id,archivo["lenguaje"])
                vulnerabilidades.append(vuln_ia1)

            if parsed_ia2.get("1.1"):

                vuln_ia2 = modelar_id_vulnerabilidad(parsed_ia2,MODELO2, archivo["file"],chunk_id,archivo["lenguaje"])
                vulnerabilidades.append(vuln_ia2)

    # -------------------------------------------------------------------
    # ----------------- PARA PRUEBAS FUNCIONALES    ---------------------
    # --------------------- METRICAS VULNERABILIDADES Y RAG -------------
    # -------------------------------------------------------------------

    vulnerabilidades = calcular_accuracy(vulnerabilidades)
    #print(">>>>> VULNERABILIDADES:")
    #print(json.dumps(vulnerabilidades, indent=4, ensure_ascii=False))

    # --------------------------------------------------
    # METRICAS DETECCIÓN VULNERABILIDADES
    # --------------------------------------------------
    metricas_det_vulns = get_metricas_deteccion_vulns(vulnerabilidades)
    print(">>>>> METRICAS SOBRE VULNERABILIDADES DETECTADAS:", metricas_det_vulns)

    logging_metricas(
        "deteccion_vulnerabilidades",
        ruta,
        metricas_det_vulns
    )

    # METRICAS RAG
    metricas_rag = get_metricas_rag(vulnerabilidades)
    print(">>>>> METRICAS SOBRE RAG:", metricas_rag)

    logging_metricas(
        "rag",
        ruta,
        metricas_rag
    )

    # --------------------------------------------------
    # METRICAS COMPARACION 
    # --------------------------------------------------
    metricas_comparativa = get_metricas_comparativa(vulnerabilidades)
    print(">>>>> METRICAS SOBRE RAG:", metricas_rag)

    logging_metricas(
        "comparativa",
        ruta,
        metricas_comparativa
    )

    # -------------------------------------------------------------------    
    # DEDUPLICACIÓN
    vulnerabilidades = deduplicar(vulnerabilidades)

    # CORRELACIÓN ENTRE VULNERABILIDADES
    ataques = correlacionar(vulnerabilidades)
    #print(">>>>> ATAQUES:")
    #print(json.dumps(ataques, indent=4, ensure_ascii=False))

    # -------------------------------------------------------------------
    # METRICAS ATAQUES CORRELACIONADOS
    # --------------------------------------------------
    ataques_detectados = ataques["ataques_detectados"]
    metricas_ataques = get_metricas_ataques(
        ataques_detectados,
        len(get_correlation_base()),
        len(vulnerabilidades)
    )
    print(">>>>> METRICAS SOBRE ATAQUES CORRELACIONADOS:", metricas_ataques)

    logging_metricas(
        "ataques_correlacionados",
        ruta,
        metricas_ataques
    )

    # -------------------------------------------------------------------    
    # GUARDAMOS EN LA BASE DE DATOS
    guardar_analisis(ruta, vulnerabilidades, ataques)
    # COMPROBAMOS LO QUE SE HA GUARDADO EN LA BD
    #test_resultados_bd()

    # --------------------------------------------------
    # PARA PRUEBAS NO FUNCIONALES
    # METRICAS NO FUNCIONALES
    # --------------------------------------------------

    tiempo_total = (time.perf_counter() - inicio_analisis)

    memoria_fin = proceso.memory_info().rss

    metricas_rendimiento = {
        "tiempo_total_segundos": round(
            tiempo_total,
            4
        ),
        "memoria_consumida_mb": round(
            (memoria_fin - memoria_inicio)
            / (1024 * 1024),
            2
        ),
        "num_archivos": len(proyecto),
        "tiempo_medio_archivo": round(
            tiempo_total / len(proyecto),
            4
        ) if proyecto else 0
    }

    print(">>>>> METRICAS RENDIMIENTO:",metricas_rendimiento)

    logging_metricas(
        "rendimiento",
        ruta,
        metricas_rendimiento
    )

    estadisticas = get_estadisticas_globales()

    # --------------------------------------------------
    # DEVOLVEMOS DATOS PARA EL FRONTEND
    # --------------------------------------------------
    return {
    "total_vulnerabilidades": len(vulnerabilidades),
    "vulnerabilidades": vulnerabilidades,
    "ataques": ataques,
    "estadisticas": estadisticas,
    # --------------------------------------------------
    # PARA PRUEBAS CON PYTEST
    "metricas_vulnerabilidades": metricas_det_vulns,
    "metricas_rag": metricas_rag,
    "metricas_comparativa": metricas_comparativa,
    "metricas_ataques": metricas_ataques,
    "metricas_rendimiento": metricas_rendimiento
}