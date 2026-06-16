
# Session Fixation (CWE-384)
function login(request, user):
    sessionId = request.getSessionId()

    # Vulnerable: no se regenera el ID de sesión tras autenticación
    session = SessionStore.get(sessionId)
    session.user = user

    return session
