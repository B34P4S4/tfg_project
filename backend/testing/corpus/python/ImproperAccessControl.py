# Improper Access Control (CWE-284)
function getUserDocument(request, documentId):
    user = request.user

    document = Database.findDocument(documentId)

    # Vulnerable: no se comprueban permisos ni propiedad del recurso
    return document.content

