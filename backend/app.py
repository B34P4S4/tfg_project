from dotenv import load_dotenv
load_dotenv()

import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.core.agents.agent import analizar_proyecto

app = Flask(__name__)
CORS(app)

@app.route("/analiza", methods=["POST"])
def analiza():

    try:

        data = request.get_json()

        if not data or "path" not in data:

            return jsonify({
                "error": "Error, falta ruta al proyecto"
            }), 400

        ruta = data["path"]

        if not os.path.exists(ruta):

            return jsonify({
                "error": "Error, ruta incorrecta. Reviselo por favor"
            }), 400

        resultados = analizar_proyecto(ruta)

        return jsonify(resultados)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)