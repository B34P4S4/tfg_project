# cargamos las variables de entorno (claves de las APIS para conectar con los modelos de IA)
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
import json

from analyzer.processor import procesar_proyecto
from core.rag.retriever import recuperar_contexto
from core.ai.prompt_builder import construir_prompt
from core.ai.client_openAI import analizar_ia1
from core.ai.client_geminiAI import analizar_ia2
from core.ai.aggregator import combinar

app = Flask(__name__)
@app.route("/analiza", methods=["POST"])

def analiza():
    try:
        data = request.get_json()

        if not data or "path" not in data:
            return jsonify({"error": "Falta el campo 'path'"}), 400

        # según la ruta que se nos haya suministrado accedemos a sus archivos para fragmentarlos (chunking)
        ruta = data["path"]
        proyecto = procesar_proyecto(ruta)

        resultados = []

        for archivo in proyecto:
            for i, chunk in enumerate(archivo["chunks"]):
                print(len(archivo["chunks"]), archivo["file"])

                # obtenemos contexto del RAG
                context = recuperar_contexto(chunk)

                # construimos el prompt
                prompt = construir_prompt(
                    context,
                    chunk,
                    file_path=archivo["file"],
                    lenguaje=archivo["lenguaje"]
                )

                # lo lanzamos a cada modelo de IA
                resultado_ia1 = analizar_ia1(prompt) # analizamos con OpenAI
                resultado_ia2 = analizar_ia2(prompt) # analizamos con Gemini                

                if isinstance(resultado_ia1, str):
                    try:
                        resultado_ia1 = json.loads(resultado_ia1)
                    except:
                        print("JSON inválido:", resultado_ia1)
                        resultado_ia1 = {"raw": resultado_ia1}

                if isinstance(resultado_ia2, str):
                    try:
                        resultado_ia2 = json.loads(resultado_ia2)
                    except:
                        print("JSON inválido:", resultado_ia2)
                        resultado_ia2 = {"raw": resultado_ia2}

                # combinamos las respuestas de ambos modelos
                res_combinado = combinar(resultado_ia1, resultado_ia2)

                # construimos JSON con toda la información por cada fragmento (chunk)
                resultados.append({
                    "file": archivo["file"],
                    "lenguaje": archivo["lenguaje"],
                    "chunk_id": i,
                    "resultado": res_combinado
                })

        return jsonify(resultados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)