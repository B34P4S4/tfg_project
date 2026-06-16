# Permissive Cross-Origin Resource Sharing (CWE-942)
function configureCORS(response):
    # Vulnerable: allows any origin and credentials
    response.setHeader("Access-Control-Allow-Origin", "*")
    response.setHeader("Access-Control-Allow-Credentials", "true")
    response.setHeader("Access-Control-Allow-Methods", "*")

    return response

