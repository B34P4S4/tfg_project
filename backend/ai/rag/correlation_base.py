# base de conocimiento con la correlacion entre vulnerabilidades con CWE que pueden indicar un posible ataque con patron CAPEC
CORRELATION_BASE = [
  {
    "id": 1,
    "nombre": "SSRF + Explotación de Metadatos",
    "descripcion": "El atacante explota una vulnerabilidad SSRF (Server-Side Request Forgery) para inducir al servidor vulnerable a realizar peticiones HTTP internas hacia servicios no expuestos públicamente, como el servicio de metadatos de instancias cloud (AWS IMDS, Azure Metadata Service o GCP Metadata). Mediante esta técnica obtiene credenciales temporales IAM, tokens de acceso o secretos internos. Posteriormente, aprovecha privilegios excesivos o controles de acceso deficientes para enumerar buckets, bases de datos, snapshots o recursos internos, provocando una exfiltración masiva de datos en entornos cloud.",
    "ataque_resultante": "Robo masivo de datos cloud",
    "capec": [
      {
        "id": 664,
        "nombre": "Server Side Request Forgery (SSRF)"
      },
      {
        "id": 118,
        "nombre": "Exploitation of Privilege/Trust"
      },
      {
        "id": 594,
        "nombre": "Traffic Injection"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Server-Side Request Forgery",
        "cwe": 918
      },
      {
        "tipo": "Improper Access Control",
        "cwe": 284
      },
      {
        "tipo": "Execution with Unnecessary Privileges",
        "cwe": 250
      }
    ]
  },
  {
    "id": 2,
    "nombre": "SQL Injection + Ejecución de Comandos",
    "descripcion": "El atacante inyecta sentencias SQL manipuladas en parámetros no validados para alterar consultas de base de datos. Tras obtener acceso al motor SQL, aprovecha funcionalidades peligrosas como xp_cmdshell, COPY TO PROGRAM o UDFs maliciosas para ejecutar comandos del sistema operativo. Una configuración insegura y privilegios excesivos permiten escalar el ataque hasta conseguir ejecución remota de código (RCE), instalar malware o desplegar ransomware sobre el servidor comprometido.",
    "ataque_resultante": "RCE y ransomware",
    "capec": [
      {
        "id": 66,
        "nombre": "SQL Injection"
      },
      {
        "id": 88,
        "nombre": "OS Command Injection"
      },
      {
        "id": 233,
        "nombre": "Privilege Escalation"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "SQL Injection",
        "cwe": 89
      },
      {
        "tipo": "Security Misconfiguration",
        "cwe": 16
      },
      {
        "tipo": "Command Injection",
        "cwe": 78
      }
    ]
  },
  {
    "id": 3,
    "nombre": "Heartbleed",
    "descripcion": "El ataque Heartbleed explota una validación incorrecta del tamaño de un paquete TLS Heartbeat en OpenSSL. Un atacante remoto envía solicitudes manipuladas indicando longitudes superiores al contenido real, provocando lecturas fuera de límites (Out-of-Bounds Read). Como resultado, el servidor devuelve fragmentos arbitrarios de memoria que pueden contener claves privadas, credenciales, cookies de sesión o información sensible residente en memoria.",
    "ataque_resultante": "Filtración de memoria y claves",
    "capec": [
      {
        "id": 540,
        "nombre": "Overread Buffers"
      },
      {
        "id": 118,
        "nombre": "Exploitation of Privilege/Trust"
      },
      {
        "id": 97,
        "nombre": "Cryptanalysis"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Improper Validation of Length Parameter",
        "cwe": 130
      },
      {
        "tipo": "Out-of-Bounds Read",
        "cwe": 126
      },
      {
        "tipo": "Information Disclosure",
        "cwe": 200
      }
    ]
  },
  {
    "id": 4,
    "nombre": "XSS + Cookies inseguras",
    "descripcion": "El atacante inyecta código JavaScript malicioso mediante una vulnerabilidad Cross-Site Scripting (XSS). Cuando la víctima accede a la aplicación, el script roba cookies de sesión que carecen de atributos de seguridad como HttpOnly o Secure. En algunos casos, el atacante fuerza además una fijación de sesión (Session Fixation), logrando secuestrar cuentas autenticadas y actuar en nombre del usuario legítimo.",
    "ataque_resultante": "Session Hijacking",
    "capec": [
      {
        "id": 63,
        "nombre": "Cross-Site Scripting"
      },
      {
        "id": 31,
        "nombre": "Session Fixation"
      },
      {
        "id": 593,
        "nombre": "Session Credential Falsification through Prediction"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Cross-Site Scripting",
        "cwe": 79
      },
      {
        "tipo": "Exposure of Sensitive Cookie Without HttpOnly",
        "cwe": 1004
      },
      {
        "tipo": "Session Fixation",
        "cwe": 384
      }
    ]
  },
  {
    "id": 5,
    "nombre": "SSTI + Deserialización insegura",
    "descripcion": "El atacante aprovecha una vulnerabilidad SSTI (Server-Side Template Injection) para ejecutar expresiones arbitrarias dentro del motor de plantillas del servidor. Posteriormente utiliza objetos serializados manipulados para desencadenar cadenas gadget durante la deserialización insegura. La combinación de ambas vulnerabilidades permite ejecutar comandos del sistema operativo, cargar payloads maliciosos y obtener ejecución remota de código completa sobre el servidor.",
    "ataque_resultante": "RCE",
    "capec": [
      {
        "id": 242,
        "nombre": "Code Injection"
      },
      {
        "id": 586,
        "nombre": "Object Injection"
      },
      {
        "id": 88,
        "nombre": "OS Command Injection"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Server-Side Template Injection",
        "cwe": 1336
      },
      {
        "tipo": "Insecure Deserialization",
        "cwe": 502
      },
      {
        "tipo": "Command Injection",
        "cwe": 78
      }
    ]
  },
  {
    "id": 6,
    "nombre": "Credential Stuffing",
    "descripcion": "El atacante automatiza intentos masivos de autenticación utilizando credenciales filtradas previamente en otras brechas de seguridad. La ausencia de mecanismos robustos de rate limiting, MFA o detección de anomalías facilita miles de intentos por minuto. Diferencias observables en las respuestas del sistema permiten validar usuarios existentes y optimizar el ataque hasta comprometer múltiples cuentas válidas.",
    "ataque_resultante": "Acceso masivo automatizado",
    "capec": [
      {
        "id": 49,
        "nombre": "Password Brute Forcing"
      },
      {
        "id": 560,
        "nombre": "Use of Known Domain Credentials"
      },
      {
        "id": 115,
        "nombre": "Authentication Abuse"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Observable Response Discrepancy",
        "cwe": 203
      },
      {
        "tipo": "Weak Authentication",
        "cwe": 307
      },
      {
        "tipo": "Missing Rate Limiting",
        "cwe": 770
      }
    ]
  },
  {
    "id": 7,
    "nombre": "CSRF + Cambio de correo",
    "descripcion": "El atacante induce a una víctima autenticada a ejecutar solicitudes HTTP no autorizadas mediante un ataque CSRF. Aprovechando la ausencia de validaciones antiforgery y controles adicionales sobre funciones críticas, modifica el correo electrónico asociado a la cuenta. Posteriormente utiliza mecanismos de recuperación de contraseña para tomar control total de la cuenta comprometida.",
    "ataque_resultante": "Account Takeover",
    "capec": [
      {
        "id": 62,
        "nombre": "Cross Site Request Forgery"
      },
      {
        "id": 115,
        "nombre": "Authentication Abuse"
      },
      {
        "id": 122,
        "nombre": "Privilege Abuse"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Cross-Site Request Forgery",
        "cwe": 352
      },
      {
        "tipo": "Missing Authentication for Critical Function",
        "cwe": 306
      },
      {
        "tipo": "Business Logic Abuse",
        "cwe": 840
      }
    ]
  },
  {
    "id": 8,
    "nombre": "Buffer Overflow + ASLR Bypass",
    "descripcion": "El atacante explota un desbordamiento de búfer sobrescribiendo memoria adyacente y alterando el flujo de ejecución del programa. Mediante técnicas de filtrado de memoria o disclosure obtiene direcciones válidas para evadir ASLR (Address Space Layout Randomization). Finalmente inyecta shellcode o construye cadenas ROP para ejecutar código arbitrario en el sistema comprometido.",
    "ataque_resultante": "Ejecución de shellcode",
    "capec": [
      {
        "id": 100,
        "nombre": "Overflow Buffers"
      },
      {
        "id": 14,
        "nombre": "Shellcode Injection"
      },
      {
        "id": 233,
        "nombre": "Privilege Escalation"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Buffer Overflow",
        "cwe": 120
      },
      {
        "tipo": "Information Disclosure",
        "cwe": 200
      },
      {
        "tipo": "Command Injection / Code Execution",
        "cwe": 78
      }
    ]
  },
  {
    "id": 9,
    "nombre": "IDOR + Exfiltración Masiva",
    "descripcion": "El atacante manipula identificadores directos de objetos (IDOR) para acceder a recursos pertenecientes a otros usuarios sin autorización. Aprovechando controles de acceso débiles y ausencia de limitación de peticiones, automatiza consultas masivas para enumerar perfiles, documentos o registros sensibles. El resultado es una exfiltración completa y silenciosa de información de clientes.",
    "ataque_resultante": "Robo completo de clientes",
    "capec": [
      {
        "id": 639,
        "nombre": "Authorization Bypass Through User-Controlled Key"
      },
      {
        "id": 118,
        "nombre": "Exploitation of Privilege/Trust"
      },
      {
        "id": 169,
        "nombre": "Footprinting"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Broken Access Control (IDOR)",
        "cwe": 284
      },
      {
        "tipo": "Missing Rate Limiting",
        "cwe": 770
      }
    ]
  },
  {
    "id": 10,
    "nombre": "LFI + Log Poisoning",
    "descripcion": "El atacante explota una vulnerabilidad Local File Inclusion (LFI) para acceder a archivos internos del servidor mediante técnicas de path traversal. Posteriormente inyecta código PHP o comandos maliciosos en archivos de log del servidor web mediante cabeceras HTTP manipuladas. Al incluir posteriormente esos logs a través de LFI, el servidor ejecuta el payload malicioso, transformando una lectura de archivos en ejecución remota de código.",
    "ataque_resultante": "LFI to RCE",
    "capec": [
      {
        "id": 126,
        "nombre": "Path Traversal"
      },
      {
        "id": 88,
        "nombre": "OS Command Injection"
      },
      {
        "id": 242,
        "nombre": "Code Injection"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Path Traversal / LFI",
        "cwe": 22
      },
      {
        "tipo": "Improper Neutralization in Logs",
        "cwe": 117
      },
      {
        "tipo": "Command Injection",
        "cwe": 78
      }
    ]
  },
  {
    "id": 11,
    "nombre": "CORS inseguro + confianza en intranet",
    "descripcion": "El atacante aprovecha una política CORS excesivamente permisiva que acepta orígenes arbitrarios o refleja dinámicamente el encabezado Origin. Desde un sitio controlado por el atacante, el navegador de la víctima autenticada realiza peticiones hacia aplicaciones internas o APIs corporativas accesibles desde la intranet. Debido a controles de acceso deficientes y confianza implícita en la red interna, el atacante obtiene información sensible y datos corporativos.",
    "ataque_resultante": "Robo de datos internos",
    "capec": [
      {
        "id": 111,
        "nombre": "JSON Hijacking"
      },
      {
        "id": 118,
        "nombre": "Exploitation of Privilege/Trust"
      },
      {
        "id": 219,
        "nombre": "Exploitation of Trusted Credentials"
      }
    ],
    "vulnerabilidades": [
      {
        "tipo": "Permissive Cross-Origin Resource Sharing",
        "cwe": 942
      },
      {
        "tipo": "Broken Access Control",
        "cwe": 284
      },
      {
        "tipo": "Information Disclosure",
        "cwe": 200
      }
    ]
  }
]