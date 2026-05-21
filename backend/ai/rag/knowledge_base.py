# base de conocimiento con las vulnerabilidades más frecuentes propias del desarrollo de código 
KNOWLEDGE_BASE = [
    {
        "1.2": "Broken Access Control (IDOR)", # A01:2025-Broken Access Control
        "1.3": "El sistema permite acceder a recursos de otros usuarios modificando un parámetro sin validación de autorización.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 1,
        "3.2": 639,
        "3.3": ["CAPEC-639", "CAPEC-233"],
        "3.4": 284, # CWE-284: Improper Access Control
        "3.5": ["T1213 Data from Information Repositories : TA0009 Collection"],
        "4.1": "Implementar controles de autorización en el backend verificando el usuario autenticado antes de acceder a recursos."
    },
    {
        "1.2": "Path Traversal", # A01:2025-Broken Access Control
        "1.3": "La aplicación permite acceder a archivos arbitrarios manipulando rutas proporcionadas por el usuario.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 1,
        "3.2": 126,
        "3.3": ["CAPEC-126"],
        "3.4": 22, # CWE-22: Improper Limitation of a Pathname to a Restricted Directory
        "3.5": ["T1005 Data from Local System : TA0009 Collection"],
        "4.1": "Validar rutas, restringir directorios accesibles y usar rutas absolutas controladas."
    },
    {
        "1.2": "Security Misconfiguration (Debug Enabled)", # A02:2025-Security Misconfiguration 
        "1.3": "La aplicación expone información sensible y functionalities internas al ejecutar el modo debug en producción.",
        "2.1": 6,
        "2.2": 4,
        "2.3": 4,
        "3.1": 2,
        "3.2": 215,
        "3.3": ["CAPEC-215", "CAPEC-233"],
        "3.4": 16, # CWE-16: Configuration
        "3.5": ["T1082 System Information Discovery : TA0007 Discovery"],
        "4.1": "Deshabilitar debug en producción, aplicar hardening y configurar correctamente servidores y frameworks."
    },
    {
        "1.2": "Vulnerable Components", # A03:2025-Software Supply Chain Failures
        "1.3": "La aplicación utiliza librerías o dependencias con vulnerabilidades conocidas y sin actualizar.",
        "2.1": 7,
        "2.2": 5,
        "2.3": 4,
        "3.1": 3,
        "3.2": 248,
        "3.3": ["CAPEC-248"],
        "3.4": 1395, # CWE-1395: Dependency on Vulnerable Third-Party Component
        "3.5": ["T1195 Supply Chain Compromise : TA0001 Initial Access"],
        "4.1": "Mantener dependencias actualizadas, usar análisis SCA y monitorizar CVEs conocidas."
    },
    {
        "1.2": "Weak Cryptography", # A04:2025-Cryptographic Failures
        "1.3": "Uso de algoritmos criptográficos débiles para almacenar contraseñas, permitiendo su recuperación mediante ataques de fuerza bruta.",
        "2.1": 7,
        "2.2": 5,
        "2.3": 3,
        "3.1": 4,
        "3.2": 326,
        "3.3": ["CAPEC-326", "CAPEC-55", "CAPEC-112"],
        "3.4": 327, # CWE-327: Use of a Broken or Risky Cryptographic Algorithm
        "3.5": ["T1555 Credentials from Password Stores : TA0006 Credential Access"],
        "4.1": "Usar algoritmos seguros como bcrypt, Argon2 o PBKDF2 con salt y políticas de gestión segura de claves."
    },
    {
        "1.2": "SQL Injection", # A05:2025-Injection
        "1.3": "La aplicación construye consultas SQL concatenando entrada del usuario sin sanitizar, permitiendo manipular la consulta.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 5,
        "3.1": 5,
        "3.2": 66,
        "3.3": ["CAPEC-66", "CAPEC-108"],
        "3.4": 89, # CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
        "3.5": ["T1190 Exploit Public-Facing Application : TA0001 Initial Access"],
        "4.1": "Usar consultas preparadas (prepared statements) y validación estricta de entradas."
    },
    {
        "1.2": "Cross-Site Scripting (XSS)", # A05:2025-Injection
        "1.3": "La aplicación inserta entrada del usuario en HTML sin sanitización permitiendo ejecución de scripts maliciosos.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 5,
        "3.2": 63,
        "3.3": ["CAPEC-63", "CAPEC-588"],
        "3.4": 79, # CWE79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
        "3.5": ["T1059 Command and Scripting Interpreter : TA0002 Execution"],
        "4.1": "Escapar salida HTML, validar entradas y utilizar CSP."
    },    
    {
        "1.2": "Command Injection", # A05:2025-Injection
        "1.3": "La aplicación ejecuta comandos del sistema usando entrada del usuario sin validación.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 5,
        "3.1": 5,
        "3.2": 88,
        "3.3": ["CAPEC-88", "CAPEC-242"],
        "3.4": 78, #CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
        "3.5": ["T1059 Command and Scripting Interpreter : TA0002 Execution"],
        "4.1": "Evitar shell=True, validar entradas y usar APIs seguras."
    },
    {
        "1.2": "Missing Threat Modeling", # A06:2025 - Insecure Design
        "1.3": "La aplicación fue diseñada sin análisis de amenazas ni controles de seguridad adecuados para proteger activos críticos.",
        "2.1": 6,
        "2.2": 4,
        "2.3": 4,
        "3.1": 6,
        "3.2": 154,
        "3.3": ["CAPEC-154"],
        "3.4": 657, # CWE-657: Violation of Secure Design Principles
        "3.5": ["T1190 Exploit Public-Facing Application : TA0001 Initial Access"],
        "4.1": "Aplicar Secure SDLC, threat modeling y principios de seguridad desde la fase de diseño."
    },

    {
        "1.2": "Business Logic Abuse", # A06:2025 - Insecure Design
        "1.3": "La lógica de negocio permite acciones no previstas como manipulación de precios, fraude o abuso de funcionalidades.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 6,
        "3.2": 840,
        "3.3": ["CAPEC-840"],
        "3.4": 840, # CWE-840: Business Logic Errors
        "3.5": ["T1659 Content Injection : TA0040 Impact"],
        "4.1": "Definir reglas de negocio seguras, validaciones de flujo y controles antifraude."
    },
    {
        "1.2": "Missing Rate Limiting in Critical Flows", # A06:2025 - Insecure Design
        "1.3": "El diseño del sistema no contempla limitación de peticiones permitiendo abuso de APIs o automatización masiva.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 6,
        "3.2": 770,
        "3.3": ["CAPEC-770","CAPEC-125"],
        "3.4": 770, # CWE-770: Allocation of Resources Without Limits or Throttling
        "3.5": ["T1499 Endpoint Denial of Service : TA0040 Impact"],
        "4.1": "Implementar rate limiting, cuotas, throttling y protección anti-bot desde el diseño arquitectónico."
    },
    {
        "1.2": "Weak Authentication (No Rate Limiting)", # A07:2025-Authentication Failures
        "1.3": "El sistema permite intentos ilimitados de login, facilitando ataques de fuerza bruta.",
        "2.1": 8,
        "2.2": 4,
        "2.3": 5,
        "3.1": 7,
        "3.2": 49,
        "3.3": ["CAPEC-49", "CAPEC-112"],
        "3.4": 307, # CWE-307: Improper Restriction of Excessive Authentication Attempts
        "3.5": ["T1110 Brute Force : TA0006 Credential Access"],
        "4.1": "Implementar limitación de intentos, bloqueo de cuentas y autenticación multifactor (MFA)."
    },
    {
        "1.2": "Hardcoded Credentials", #A07:2025 - Authentication Failures        
        "1.3": "La aplicación contiene credenciales embebidas en el código fuente.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 7,
        "3.2": 798,
        "3.3": ["CAPEC-798"],
        "3.4": 798, # CWE-798: Use of Hard-coded Credentials
        "3.5": ["T1552 Unsecured Credentials : TA0006 Credential Access"],
        "4.1": "Usar gestores de secretos y variables de entorno."
    },  
    {
        "1.2": "Insecure Deserialization", # A08:2025-Software or Data Integrity Failures
        "1.3": "La aplicación deserializa datos no confiables permitiendo ejecución de código arbitrario.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 5,
        "3.1": 8,
        "3.2": 586,
        "3.3": ["CAPEC-586", "CAPEC-502"],
        "3.4": 502, # CWE-502: Deserialization of Untrusted Data
        "3.5": ["T1059 Command and Scripting Interpreter : TA0002 Execution"],
        "4.1": "Evitar deserialización insegura, validar integridad de datos y usar formatos seguros como JSON."
    },
    {
        "1.2": "Insufficient Logging and Monitoring", # A09:2025-Security Logging and Alerting Failures
        "1.3": "La aplicación no registra ni monitoriza eventos críticos de seguridad dificultando la detección de ataques.",
        "2.1": 5,
        "2.2": 3,
        "2.3": 3,
        "3.1": 9,
        "3.2": 223,
        "3.3": ["CAPEC-223"],
        "3.4": 778, # CWE-778: Insufficient Logging
        "3.5": ["T1070 Indicator Removal on Host : TA0005 Defense Evasion"],
        "4.1": "Implementar logging centralizado, alertas automáticas y monitorización continua de eventos."
    },
    {
        "1.2": "Server-Side Request Forgery (SSRF)", # A10:2025 - Mishandling of Exceptional Conditions
        "1.3": "La aplicación realiza peticiones HTTP a URLs controladas por el usuario permitiendo acceso a recursos internos.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 10,
        "3.2": 664,
        "3.3": ["CAPEC-664"],
        "3.4": 918, # CWE-918: Server-Side Request Forgery
        "3.5": ["T1110 Brute Force : TA0006 Credential Access"], 
        "4.1": "Validar URLs, usar allowlists y restringir conexiones salientes desde el servidor."
    }
]
