# base de conocimiento con las vulnerabilidades más frecuentes propias del desarrollo de código 
KNOWLEDGE_BASE = [
    {
        "1.2": "Broken Access Control (IDOR)", # A01:2025-Broken Access Control
        "1.3": "El sistema permite acceder a recursos de otros usuarios modificando un parámetro sin validación de autorización.", # descripcion
        "2.1": 8, # cvss
        "2.2": 5, # impacto (1-5)
        "2.3": 4, # probabilidad (1-5)
        "3.1": 1, # OWASP TOP 10
        "3.2": 639, # CAPEC
        "3.3": ["CAPEC-639", "CAPEC-233"],
        "3.4": 284, # CWE-284: Improper Access Control
        "3.5": ["T1213 Data from Information Repositories : TA0009 Collection"], # TECNICAS Y TACTICAS MITRE RELACIONADAS CON CWE
        "4.1": "Implementar controles de autorización en el backend verificando el usuario autenticado antes de acceder a recursos." # mitigacion
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
        "1.2": "Cross-Site Request Forgery (CSRF)", # A01:2025-Broken Access Control
        "1.3": "La aplicación acepta solicitudes autenticadas sin verificar origen ni tokens antiforgery.",
        "2.1": 6,
        "2.2": 4,
        "2.3": 4,
        "3.1": 1,
        "3.2": 62,
        "3.3": ["CAPEC-62"],
        "3.4": 352, # CWE-352: Cross-Site Request Forgery (CSRF)
        "3.5": ["T1185 Browser Session Hijacking : TA0006 Credential Access"],
        "4.1": "Usar tokens CSRF y validar origen/referer."
    },
    {
        "1.2": "Permissive CORS", # A01:2025-Broken Access Control
        "1.3": "La política Cross-domain Security permite acceso desde orígenes no confiables.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 1,
        "3.2": 111,
        "3.3": ["CAPEC-111"],
        "3.4": 942, # CWE-942: Permissive Cross-domain Security Policy with Untrusted Domains
        "3.5": ["T1539 Steal Web Session Cookie : TA0006 Credential Access"],
        "4.1": "Restringir Access-Control-Allow-Origin a dominios confiables."
    },
    {
        "1.2": "Execution with Unnecessary Privileges", # A01:2025-Broken Access Control
        "1.3": "La aplicación o servicio se ejecuta con privilegios superiores a los necesarios, permitiendo que un atacante amplifique el impacto de una explotación y acceda a recursos críticos del sistema o del entorno cloud.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 1,
        "3.2": 233,
        "3.3": ["CAPEC-233","CAPEC-122"],
        "3.4": 250, # CWE-250: Execution with Unnecessary Privileges
        "3.5": ["T1068 Exploitation for Privilege Escalation : TA0004 Privilege Escalation",
        "T1548 Abuse Elevation Control Mechanism : TA0004 Privilege Escalation",
        "T1078 Valid Accounts : TA0001 Initial Access"],
        "4.1": "Aplicar el principio de mínimo privilegio, ejecutar servicios con cuentas restringidas y limitar permisos IAM, sudo o root únicamente a operaciones necesarias."
    },
    {
        "1.2": "Path Traversal: Multiple Leading Traversal Sequences", # A01:2025-Broken Access Control
        "1.3": "La aplicación no neutraliza correctamente secuencias de traversal repetidas como '../../../', permitiendo acceder a archivos o directorios fuera de las rutas autorizadas.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 1,
        "3.2": 126,
        "3.3": ["CAPEC-126","CAPEC-64"],
        "3.4": 31, # CWE-31: Path Traversal: 'dir\..\..\filename'
        "3.5": ["T1005 Data from Local System : TA0009 Collection","T1083 File and Directory Discovery : TA0007 Discovery"],
        "4.1": "Normalizar rutas, bloquear secuencias de traversal y restringir el acceso a directorios permitidos mediante allowlists."
    },
    {
        "1.2": "Information Disclosure", # A01:2025-Broken Access Control
        "1.3": "La aplicación expone información sensible a usuarios no autorizados mediante respuestas, errores, logs, memoria, metadatos o configuraciones inseguras.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 1,
        "3.2": 118,
        "3.3": ["CAPEC-118","CAPEC-169"],
        "3.4": 200, # CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
        "3.5": ["T1005 Data from Local System : TA0009 Collection",
        "T1213 Data from Information Repositories : TA0009 Collection",
        "T1083 File and Directory Discovery : TA0007 Discovery"],
        "4.1": "Minimizar la exposición de información sensible, aplicar controles de acceso y evitar mensajes de error detallados en producción."
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
        "1.2": "Server-Side Template Injection (SSTI)", # A05:2025-Injection
        "1.3": "El motor de plantillas evalúa expresiones controladas por el usuario permitiendo ejecución de código.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 4,
        "3.1": 5,
        "3.2": 242,
        "3.3": ["CAPEC-242"],
        "3.4": 1336, # CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine
        "3.5": ["T1059 Command and Scripting Interpreter : TA0002 Execution"],
        "4.1": "Deshabilitar evaluación dinámica y usar sandboxing."
    },
    {
        "1.2": "Buffer Overflow", # A05:2025-Injection
        "1.3": "La aplicación escribe datos fuera de los límites de memoria asignados.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 4,
        "3.1": 5,
        "3.2": 100,
        "3.3": ["CAPEC-100", "CAPEC-14"],
        "3.4": 120, # CWE-120: Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')
        "3.5": ["T1068 Exploitation for Privilege Escalation : TA0004 Privilege Escalation"],
        "4.1": "Validar tamaños de entrada y usar protecciones ASLR/DEP/Canaries."
    },
    {
        "1.2": "Improper Validation of Length Parameter", # A05:2025-Injection
        "1.3": "La aplicación no valida correctamente los parámetros de longitud utilizados en operaciones de memoria o procesamiento de datos, permitiendo lecturas o escrituras fuera de los límites esperados.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 5,
        "3.2": 540,
        "3.3": ["CAPEC-540","CAPEC-100"],
        "3.4": 130, # CWE-130: Improper Handling of Length Parameter Inconsistency
        "3.5": ["T1203 Exploitation for Client Execution : TA0002 Execution","T1068 Exploitation for Privilege Escalation : TA0004 Privilege Escalation"],
        "4.1": "Validar estrictamente tamaños y límites antes de procesar buffers, paquetes o estructuras de memoria."
    },
    {
        "1.2": "Out-of-Bounds Read", # A05:2025-Injection
        "1.3": "La aplicación lee posiciones de memoria fuera de los límites asignados a un buffer, exponiendo información sensible como credenciales, claves o datos internos.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 4,
        "3.1": 5,
        "3.2": 540,
        "3.3": ["CAPEC-540","CAPEC-118"],
        "3.4": 126, # CWE-126: Buffer Over-read
        "3.5": ["T1005 Data from Local System : TA0009 Collection",
        "T1213 Data from Information Repositories : TA0009 Collection"],
        "4.1": "Implementar validaciones de límites de memoria y utilizar lenguajes o librerías con protección de memoria."
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
        "3.2": 233,
        "3.3": ["CAPEC-233", "CAPEC-122"],
        "3.4": 840, # CWE-840: Business Logic Errors
        "3.5": ["T1659 Content Injection : TA0040 Impact"],
        "4.1": "Definir reglas de negocio seguras, validaciones de flujo y controles antifraude."
    },
    {
        "1.2": "Missing Rate Limiting in Critical Flows", # A06:2025 - Insecure Design
        "1.3": "El diseño del sistema no contempla limitación de peticiones permitiendo automatización masiva o ataques de fuerza bruta.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 6,
        "3.2": 125,
        "3.3": ["CAPEC-125"],
        "3.4": 770, # CWE-770: Allocation of Resources Without Limits or Throttling
        "3.5": ["T1110 Brute Force : TA0006 Credential Access",
        "T1499 Endpoint Denial of Service : TA0040 Impact"],
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
        "3.2": 37,
        "3.3": ["CAPEC-37"],
        "3.4": 798, # CWE-798: Use of Hard-coded Credentials
        "3.5": ["T1552 Unsecured Credentials : TA0006 Credential Access"],
        "4.1": "Usar gestores de secretos y variables de entorno."
    },
    {
        "1.2": "Session Credential Falsification through Prediction", #A07:2025 - Authentication Failures  
        "1.3": "La aplicación utiliza identificadores de sesión predecibles o fácilmente adivinables, permitiendo a un atacante secuestrar sesiones válidas y autenticarse como otros usuarios.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 7,
        "3.2": 593,
        "3.3": ["CAPEC-593","CAPEC-31"],
        "3.4": 593, # CWE-593: Authentication Bypass: OpenSSL CTX Object Modified after SSL Objects are Created
        "3.5": ["T1539 Steal Web Session Cookie : TA0006 Credential Access","T1078 Valid Accounts : TA0001 Initial Access"],
        "4.1": "Generar identificadores de sesión criptográficamente aleatorios, regenerar sesiones tras autenticación y configurar cookies seguras con HttpOnly y Secure."
    },
    {
        "1.2": "Sensitive Cookie Without HttpOnly", #A07:2025 - Authentication Failures  
        "1.3": "La aplicación establece cookies sensibles sin el atributo HttpOnly, permitiendo que scripts ejecutados en el navegador accedan al identificador de sesión y faciliten ataques de robo de sesión mediante XSS.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 7,
        "3.2": 63,
        "3.3": ["CAPEC-63","CAPEC-593","CAPEC-31"],
        "3.4": 1004, # 	CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag
        "3.5": ["T1539 Steal Web Session Cookie : TA0006 Credential Access","T1185 Browser Session Hijacking : TA0006 Credential Access"],
        "4.1": "Configurar las cookies sensibles con los atributos HttpOnly, Secure y SameSite para impedir acceso desde JavaScript y reducir el riesgo de secuestro de sesión."
    },
    {
        "1.2": "Session Fixation", #A07:2025 - Authentication Failures  
        "1.3": "El atacante fuerza o predice un identificador de sesión válido y consigue que la víctima lo utilice tras autenticarse, permitiendo reutilizar esa sesión para acceder a la cuenta sin necesidad de credenciales.",
        "2.1": 8,
        "2.2": 5,
        "2.3": 4,
        "3.1": 7,
        "3.2": 31,
        "3.3": ["CAPEC-31","CAPEC-593"],
        "3.4": 384, # CWE-384: Session Fixation
        "3.5": ["T1539 Steal Web Session Cookie : TA0006 Credential Access","T1185 Browser Session Hijacking : TA0006 Credential Access","T1078 Valid Accounts : TA0001 Initial Access"],
        "4.1": "Regenerar el identificador de sesión tras login, invalidar sesiones antiguas y usar cookies seguras con HttpOnly, Secure y SameSite."
    },
    {
        "1.2": "Observable Response Discrepancy", #A07:2025 - Authentication Failures  
        "1.3": "La aplicación devuelve respuestas diferentes según el estado de autenticación o la existencia de recursos, lo que permite a un atacante inferir información sensible como usuarios válidos, existencia de cuentas o estructura interna del sistema.",
        "2.1": 6,
        "2.2": 4,
        "2.3": 4,
        "3.1": 7,
        "3.2": 203,
        "3.3": ["CAPEC-203","CAPEC-208"],
        "3.4": 203, # CWE-203: Observable Discrepancy
        "3.5": ["T1598 Phishing for Information : TA0043 Reconnaissance",
        "T1083 File and Directory Discovery : TA0007 Discovery",
        "T1010 Application Window Discovery : TA0007 Discovery"],
        "4.1": "Unificar respuestas del sistema para evitar filtrado de información, aplicar rate limiting y evitar diferencias observables en errores o tiempos de respuesta."
    },
    {
        "1.2": "Missing Authentication for Critical Function", #A07:2025 - Authentication Failures  
        "1.3": "La aplicación permite ejecutar funciones críticas (como cambios de correo, reset de contraseña o modificación de privilegios) sin requerir autenticación o verificación adicional, lo que facilita el secuestro de cuentas o la alteración no autorizada de datos sensibles.",
        "2.1": 9,
        "2.2": 5,
        "2.3": 4,
        "3.1": 7,
        "3.2": 122,
        "3.3": ["CAPEC-122","CAPEC-114"],
        "3.4": 306, # CWE-306: Missing Authentication for Critical Function
        "3.5": ["T1098 Account Manipulation : TA0006 Credential Access",
        "T1556 Modify Authentication Process : TA0006 Credential Access",
        "T1078 Valid Accounts : TA0001 Initial Access"],
        "4.1": "Exigir autenticación reforzada (MFA o reautenticación) para operaciones críticas y validar siempre permisos en backend antes de ejecutar cambios sensibles."
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
        "1.2": "Improper Neutralization of Input in Log Outputs (Log Injection / Log Poisoning)", # A09:2025-Security Logging and Alerting Failures
        "1.3": "La aplicación no neutraliza adecuadamente las entradas del usuario antes de registrarlas en logs, lo que permite inyectar contenido malicioso, manipular registros, ocultar actividad o incluso facilitar ejecución de código si los logs son interpretados por otros sistemas.",
        "2.1": 7,
        "2.2": 4,
        "2.3": 4,
        "3.1": 9,
        "3.2": 117,
        "3.3": ["CAPEC-117","CAPEC-93"],
        "3.4": 117, # CWE-117: Improper Output Neutralization for Logs
        "3.5": ["T1070 Indicator Removal on Host : TA0005 Defense Evasion",
        "T1056 Input Capture : TA0006 Credential Access",
        "T1005 Data from Local System : TA0009 Collection"],
        "4.1": "Aplicar sanitización estricta de entradas antes del logging, usar encoding seguro en logs estructurados y evitar que los registros sean interpretados como código por sistemas posteriores."
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
        "3.5": ["T1190 Exploit Public-Facing Application : TA0001 Initial Access",
        "T1213 Data from Information Repositories : TA0009 Collection",
        "T1552 Unsecured Credentials : TA0006 Credential Access"], 
        "4.1": "Validar URLs, usar allowlists y restringir conexiones salientes desde el servidor."
    }
]
