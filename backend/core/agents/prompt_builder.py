def construir_prompt(context, code, file_path=None, lenguaje=None):
    
    # construimos primero el contexto desde el RAG
    context_text = "\n".join(
        [
            f"{c['1.2']} | CWE-{c['3.4']} | CAPEC-{c['3.2']} | OWASP A{c['3.1']}\n"
            f"Desc: {c['1.3']}\n"
            f"Mitigación: {c['4.1']}\n"
            f"Riesgo: CVSS {c['2.1']} (Impacto {c['2.2']}/5, Prob {c['2.3']}/5)\n"
            for c in context
        ]
    )

    print("CONTEXTO DEL RAG:", context_text)

    # montamos el prompt para las IA
    return f"""
    Eres un auditor de código software.
    Dispones del siguiente contexto de vulnerabilidades de código conocidas:{context_text}

    INSTRUCCIONES:
    - Utiliza el contexto proporcionado para identificar vulnerabilidades similares
    - Si el código coincide con alguna vulnerabilidad del contexto, indícalo explícitamente
    - Si no hay coincidencia exacta, razona posibles vulnerabilidades basadas en el contexto

    Analiza el siguiente código fuente y determina si contiene vulnerabilidades de seguridad:
    - Archivo: {file_path if file_path else "desconocido"}
    - Lenguaje: {lenguaje if lenguaje else "desconocido"}

    Devuelve exclusivamente un objeto JSON válido (sin texto adicional) con la siguiente estructura exacta:
    {{
      "1.1": boolean,
      "1.2": "string",
      "1.3": "string",
      "1.4": number,
      "1.5": number,
      "2.1": number,
      "2.2": number,
      "2.3": number,
      "3.1": number,
      "3.2": number,
      "3.3": ["string"],
      "3.4": number,
      "3.5": ["string"],
      "4.1": ["string"]
    }}

    Reglas obligatorias:
    - "1.1": true si el código es vulnerable, false si no lo es.
    - "1.2": nombre de la vulnerabilidad (ej: "SQL Injection").
    - "1.3": explicación breve y clara (máximo 2-3 líneas).
    - "1.4": indica la línea exacta donde entra (source) el input vulnerable (entero).
    - "1.5": indica la línea exacta donde se ejecuta (sink) la vulnerabilidad (entero).
    - "2.1": nivel CVSS 3.0 simplificado de 0 a 10 (entero).
    - "2.2": impacto de 1 a 5 (entero).
    - "2.3": probabilidad de 1 a 5 (entero).
    - "3.1": posición en OWASP Top 10 (1-10, entero).
    - "3.2": código CAPEC principal en formato numérico.
    - "3.3": lista de códigos CAPEC relacionados (formato: "CAPEC-XXX").
    - "3.4": código CWE principal en formato numérico.
    - "3.5": lista de técnicas MITRE ATT&CK en formato:
      "TXXXX Nombre de la técnica : TAXXXX Nombre de la táctica".
    - "4.1": qué y cómo se corrige o mitiga, explicación breve y clara (máximo 2-3 líneas).

    Restricciones estrictas:
    - No incluyas texto fuera del JSON.
    - No incluyas Markdown ni bloques de código.
    - No incluyas comentarios.
    - Escapa todas las barras invertidas según la especificación JSON.
    - No incluyas rutas Windows con '\' sin escapar.
    - Usa únicamente los tipos indicados (boolean, number, string, array).
    - Los números deben ir sin comillas.
    - Si no aplica algún campo, devuelve un valor razonable (por ejemplo, 0 o lista vacía).
    - Si "1.1" es true, entonces "3.2", "3.4" y "3.5" NO pueden estar vacíos.

    Código a analizar:
    {code}
    """
