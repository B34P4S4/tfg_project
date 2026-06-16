
# Command Injection (CWE-78)
function runDiagnostic(userInput):
    command = "diagnostic_tool " + userInput

    # Vulnerable: ejecución directa de comando construido con input
    result = System.execute(command)
    return result