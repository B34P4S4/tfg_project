# Command Injection (CWE-78)
function runMaintenance(userInput):
    command = "maintenance_tool " + userInput

    # Vulnerable: unsanitized input used in system command
    System.execute(command)

    return "maintenance executed"