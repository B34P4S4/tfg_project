# Improper Neutralization in Logs (CWE-117)
function logUserAction(userInput):
    logEntry = "User action: " + userInput

    # Vulnerable: no sanitization before writing to logs
    Logger.write(logEntry)

    return "logged"



