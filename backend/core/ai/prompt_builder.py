def construir_prompt(code, file_path=None, lenguaje=None):
    return f"""
    Analiza el siguiente código fuente y determina si contiene vulnerabilidades de seguridad.

    Contexto del análisis:
    - Archivo: {file_path if file_path else "desconocido"}
    - Lenguaje: {lenguaje if lenguaje else "desconocido"}

    Devuelve exclusivamente un objeto JSON válido (sin texto adicional) con la siguiente estructura exacta:
    {{
      "1.1": boolean,
      "1.2": "string",
      "1.3": "string",
      "1.4": "string",
      "1.5": "string",
      "2.1": number,
      "2.2": number,
      "2.3": number,
      "3.1": number,
      "3.2": number,
      "3.3": number,
      "3.4": ["string"],
      "3.5": ["string"]
    }}

    Reglas obligatorias:
    - "1.1": true si el código es vulnerable, false si no lo es.
    - "1.2": nombre de la vulnerabilidad (ej: "SQL Injection").
    - "1.3": explicación breve y clara (máximo 2-3 líneas).
    - "1.4": indica la línea exacta donde entra el input vulnerable.
    - "1.5": indica la línea exacta donde se ejecuta la vulnerabilidad.
    - "2.1": nivel CVSS simplificado de 1 a 4 (entero).
    - "2.2": impacto de 1 a 5 (entero).
    - "2.3": probabilidad de 1 a 5 (entero).
    - "3.1": posición en OWASP Top 10 (1-10, entero).
    - "3.2": código CAPEC principal en formato numérico.
    - "3.3": código CWE principal en formato numérico.
    - "3.4": lista de códigos CAPEC relacionados (formato: "CAPEC-XXX").
    - "3.5": lista de técnicas MITRE ATT&CK en formato:
      "TXXXX Nombre de la técnica : TAXXXX Nombre de la táctica".

    Restricciones estrictas:
    - No incluyas texto fuera del JSON.
    - No incluyas Markdown ni bloques de código.
    - No incluyas comentarios.
    - Usa únicamente los tipos indicados (boolean, number, string, array).
    - Los números deben ir sin comillas.
    - Si no aplica algún campo, devuelve un valor razonable (por ejemplo, 0 o lista vacía).
    - Si "1.1" es true, entonces "3.4" y "3.5" NO pueden estar vacíos.

    Código a analizar:
    {code}
    """
