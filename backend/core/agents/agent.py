from backend.core.processing.repository.processor import procesar_proyecto

from backend.ai.rag.retriever import recuperar_contexto
from backend.ai.rag.init_rag import init_vector_store

from backend.core.agents.prompt_builder import construir_prompt
from backend.core.parsing.parser import parsear_salida_IA
from backend.core.parsing.deduplicator import deduplicar
from backend.core.processing.vulnerability.processor_vul import modelar_id_vulnerabilidad
from backend.core.processing.vulnerability.correlator_vul import correlacionar

from backend.ai.models.client_openAI import analizar_ia1
from backend.ai.models.client_geminiAI import analizar_ia2


# inicializamos RAG 
vector_store = init_vector_store()
print("VECTOR STORE agent:", vector_store)

MODELO1 = "openAI"
MODELO2 = "gemini"

# --------------------------------------------
# PIPELINE PRINCIPAL
# --------------------------------------------

def analizar_proyecto(ruta):

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

    
    # DEDUPLICACIÓN
    vulnerabilidades = deduplicar(vulnerabilidades)

    # CORRELACIÓN ENTRE VULNERABILIDADES
    ataques = correlacionar(vulnerabilidades)

    return {
    "total_vulnerabilidades": len(vulnerabilidades),
    "vulnerabilidades": vulnerabilidades,
    "ataques": ataques
}