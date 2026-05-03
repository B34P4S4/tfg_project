# CARGAMOS VARIABLES DE ENTORNO
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
import json

from analyzer.processor import procesar_proyecto
from core.ai.prompt_builder import build_prompt
from core.ai.client_openAI import analyze_with_ai

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data or "path" not in data:
            return jsonify({"error": "Falta el campo 'path'"}), 400

        ruta = data["path"]
        language = data.get("language", "python")

        proyecto = procesar_proyecto(ruta)
        prompt = build_prompt(proyecto, language)

        ai_result = analyze_with_ai(prompt)

        # 🔥 IMPORTANTE: asegurar que es dict
        if isinstance(ai_result, str):
            ai_result = json.loads(ai_result)

        return jsonify(ai_result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)