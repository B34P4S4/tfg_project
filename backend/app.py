from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from backend.core.agents.agent import analizar_proyecto

app = Flask(__name__)

@app.route("/analiza", methods=["POST"])
def analiza():

    try:
        data = request.get_json()

        if not data or "path" not in data:
            return jsonify({
                "error": "Falta el campo 'path'"
            }), 400

        ruta = data["path"]
        resultados = analizar_proyecto(ruta)

        return jsonify(resultados)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)