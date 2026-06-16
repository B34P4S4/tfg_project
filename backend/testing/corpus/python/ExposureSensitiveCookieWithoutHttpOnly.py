# Exposure of Sensitive Cookie Without HttpOnly (CWE-1004)
function setSessionCookie(response, sessionId):
    cookie = "sessionId=" + sessionId + "; Path=/"
    
    # Vulnerable: cookie sin HttpOnly ni Secure
    response.setHeader("Set-Cookie", cookie)
    return response

