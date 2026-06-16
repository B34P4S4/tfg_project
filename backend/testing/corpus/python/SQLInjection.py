# SQL Injection (CWE-89)
function getUserById(userId):
    query = "SELECT * FROM users WHERE id = " + userId
    result = Database.execute(query)
    return result


