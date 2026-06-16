# Missing Authentication for Critical Function (CWE-306)
function deleteAllUsers(request):
    # Vulnerable: no authentication or authorization check
    Database.deleteAllUsers()

    return "All users deleted"


