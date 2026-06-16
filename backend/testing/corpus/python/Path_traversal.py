# Path Traversal / Local File Inclusion (CWE-22)
function readFile(userInputPath):
    basePath = "/app/files/"

    # Vulnerable: no sanitization of path traversal sequences
    fullPath = basePath + userInputPath

    fileContent = FileSystem.read(fullPath)
    return fileContent


