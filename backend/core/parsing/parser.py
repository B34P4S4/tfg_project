# damos forma a la salida de los modelos IA 
import json

def parsear_salida_IA(output):
    try:
        if isinstance(output, dict):
            return output

        output = output.strip()

        if output.startswith("```"):
            output = (
                output
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(output)

    except json.JSONDecodeError:
        return {
            "1.1": False,
            "1.2": "",
            "1.3": "",
            "1.4": 0,
            "1.5": 0,
            "2.1": 0,
            "2.2": 0,
            "2.3": 0,
            "3.1": 0,
            "3.2": 0,
            "3.3": [],
            "3.4": 0,
            "3.5": [],
            "4.1": []
        }




