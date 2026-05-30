import re
import json

import google.generativeai as genai
from backend.config import GEMINI_API_KEY,GEMINI_MODEL,TIMEOUT_GEMINI

genai.configure(api_key=GEMINI_API_KEY)
print("GEMINI_MODEL =", GEMINI_MODEL)

def analizar_ia2(prompt):
    
    try:
        model = genai.GenerativeModel(GEMINI_MODEL)

        full_prompt = f"""
        {prompt}      
        """
        response = model.generate_content(prompt)
        text = response.text.strip()
        print("RAW:", text)

        # limpiamos para que tenga forma de JSON
        if text.startswith("```"):
            text = re.sub(r"^```json\s*", "", text)
            text = re.sub(r"^```", "", text)
            text = re.sub(r"\s*```$", "", text)

        data = json.loads(text)

        return data

    except Exception as e:
        print("ERROR IA:", repr(e))
        raise e   # si no obtenemos respuesta de Gemini nos indicará qué ha ocurrido