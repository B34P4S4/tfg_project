import os
import re
import json
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analizar_ia2(prompt):
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

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