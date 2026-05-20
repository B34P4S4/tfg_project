# base de conocimiento con las vulnerabilidades más frecuentes propias del desarrollo de código 
KNOWLEDGE_BASE = [
    {
        "1.2": "Broken Access Control (IDOR)", # A01: Broken Access Control
        "1.3": "El sistema permite acceder a recursos de otros usuarios modificando un parámetro sin validación de autorización.",
        "1.4": 12,
        "1.5": 18,
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 1,
        "3.2": 639,
        "3.3": ["CAPEC-639", "CAPEC-233"],
        "3.4": 284,
        "3.5": ["T1213 Data from Information Repositories : TA0009 Collection"],
        "4.1": "Implementar controles de autorización en el backend verificando el usuario autenticado antes de acceder a recursos."
    },
    {
        "1.2": "Weak Cryptography (MD5)", # A04: Cryptographic Failures
        "1.3": "Uso de algoritmos criptográficos débiles para almacenar contraseñas, permitiendo su recuperación mediante ataques de fuerza bruta.",
        "1.4": 8,
        "1.5": 15,
        "2.1": 7,
        "2.2": 5,
        "2.3": 3,
        "3.1": 4,
        "3.2": 326,
        "3.3": ["CAPEC-55", "CAPEC-112"],
        "3.4": 327,
        "3.5": ["T1555 Credentials from Password Stores : TA0006 Credential Access"],
        "4.1": "Usar algoritmos seguros como bcrypt, Argon2 o PBKDF2 con salt y políticas de gestión segura de claves."
    },
    {
        "1.2": "SQL Injection", # A05: Injection (SQL, command, etc.)
        "1.3": "La aplicación construye consultas SQL concatenando entrada del usuario sin sanitizar, permitiendo manipular la consulta.",
        "1.4": 10,
        "1.5": 14,
        "2.1": 9,
        "2.2": 5,
        "2.3": 5,
        "3.1": 5,
        "3.2": 66,
        "3.3": ["CAPEC-66", "CAPEC-108"],
        "3.4": 89,
        "3.5": ["T1190 Exploit Public-Facing Application : TA0001 Initial Access"],
        "4.1": "Usar consultas preparadas (prepared statements) y validación estricta de entradas."
    },
    {
        "1.2": "Weak Authentication (No Rate Limiting)", # A07: Authentication Failures
        "1.3": "El sistema permite intentos ilimitados de login, facilitando ataques de fuerza bruta.",
        "1.4": 6,
        "1.5": 12,
        "2.1": 8,
        "2.2": 4,
        "2.3": 5,
        "3.1": 7,
        "3.2": 49,
        "3.3": ["CAPEC-49", "CAPEC-112"],
        "3.4": 307,
        "3.5": ["T1110 Brute Force : TA0006 Credential Access"],
        "4.1": "Implementar limitación de intentos, bloqueo de cuentas y autenticación multifactor (MFA)."
    }
]
