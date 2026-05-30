from openai import OpenAI
from backend.config import OPENAI_API_KEY,OPENAI_MODEL,TIMEOUT_OPENAI

client = OpenAI(api_key=OPENAI_API_KEY)
print("OPENAI_MODEL =", OPENAI_MODEL)


def analizar_ia1(prompt):
   
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            timeout=TIMEOUT_OPENAI  # lanzamos consulta a OpenAI cada 30 segundos
        )

        print("Respuesta recibida de OpenAI")
        return response.choices[0].message.content

    except Exception as e:
        print("ERROR IA:", e)  # si no obtenemos respuesta de OpenAI nos indicará qué ha ocurrido
        return "{}"
