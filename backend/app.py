from backend.config import HOST, PORT, DEBUG

import os

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from backend.core.agents.agent import analizar_proyecto
from backend.core.reporting.reporter import generar_reporte_pdf

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

@app.route("/exportar", methods=["POST"])
def exportar():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No hay datos"
            }), 400

        pdf_path = generar_reporte_pdf(data)

        return send_file(
            pdf_path,
            as_attachment=True
        )

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)