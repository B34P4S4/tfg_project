from flask import Flask, request, jsonify
from analyzer.processor import procesar_proyecto

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    ruta = request.json.get("path")

    resultado = procesar_proyecto(ruta)

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)