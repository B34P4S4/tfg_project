# Server-Side Request Forgery (CWE-918)
function fetchRemoteData(userInputUrl):
    # Vulnerable: usa directamente entrada del usuario sin validación
    response = HTTPClient.get(userInputUrl)
    return response.body


