# Observable Response Discrepancy (CWE-203)
function checkUserExists(username):
    user = Database.findUser(username)

    if user != null:
        return "User found"
    else:
        return "Invalid username or password"  # Vulnerable: filtra información sobre existencia de usuarios


