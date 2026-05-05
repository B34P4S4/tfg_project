import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analizar_ia(prompt):
   
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            timeout=30
        )

        print("Respuesta recibida")

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR IA:", e)
        return "{}"
