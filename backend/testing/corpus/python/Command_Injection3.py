
# Command Injection (CWE-78)
function executeBackup(userInputPath):
    command = "backup_tool " + userInputPath
    result = System.execute(command)
    return result