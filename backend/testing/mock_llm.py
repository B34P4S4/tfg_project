import random

def analizar_codigo_mock(chunk):
    vulnerabilidades = []

    texto = chunk.lower()

    if "select" in texto and "+" in texto:
        vulnerabilidades.append({
            "type": "SQL Injection",
            "cwe": "CWE-89",
            "severity": "HIGH",
            "line": random.randint(1, 100),
            "description": "Posible SQL Injection por concatenación de strings.",
            "recommendation": "Usar consultas parametrizadas."
        })

    if "eval(" in texto:
        vulnerabilidades.append({
            "type": "Code Injection",
            "cwe": "CWE-94",
            "severity": "HIGH",
            "line": random.randint(1, 100),
            "description": "Uso inseguro de eval().",
            "recommendation": "Evitar eval() o validar entradas."
        })

    if "password" in texto:
        vulnerabilidades.append({
            "type": "Hardcoded Credentials",
            "cwe": "CWE-522",
            "severity": "MEDIUM",
            "line": random.randint(1, 100),
            "description": "Posible contraseña en texto plano.",
            "recommendation": "Usar variables de entorno."
        })

    return vulnerabilidades