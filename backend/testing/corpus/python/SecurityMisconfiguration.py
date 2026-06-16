# Security Misconfiguration (CWE-16)
function startDebugMode(app):
    # Vulnerable: configuración insegura habilitada en producción
    app.config.debug = true
    app.config.showDetailedErrors = true
    app.config.allowAllOrigins = true

    return app

