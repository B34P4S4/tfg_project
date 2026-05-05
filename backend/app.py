# CARGAMOS VARIABLES DE ENTORNO
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
import json

from analyzer.processor import procesar_proyecto
from core.ai.prompt_builder import construir_prompt
from core.ai.client_openAI import analizar_ia

app = Flask(__name__)
@app.route("/analiza", methods=["POST"])

def analiza():
    try:
        data = request.get_json()

        if not data or "path" not in data:
            return jsonify({"error": "Falta el campo 'path'"}), 400

        ruta = data["path"]
        proyecto = procesar_proyecto(ruta)

        resultados = []

        for archivo in proyecto:
            for i, chunk in enumerate(archivo["chunks"]):
                print(len(archivo["chunks"]), archivo["file"])

                prompt = construir_prompt(
                    chunk,
                    file_path=archivo["file"],
                    lenguaje=archivo["lenguaje"]
                )

                resultado_ia = analizar_ia(prompt)

                if isinstance(resultado_ia, str):
                    resultado_ia = json.loads(resultado_ia)

                resultados.append({
                    "file": archivo["file"],
                    "lenguaje": archivo["lenguaje"],
                    "chunk_id": i,
                    "resultado": resultado_ia
                })

        return jsonify(resultados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)