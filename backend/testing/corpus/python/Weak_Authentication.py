# Weak Authentication (CWE-307)
function login(username, password):
    user = Database.findUser(username)

    # Vulnerable: sin protección contra intentos repetidos ni MFA
    if user.password == password:
        return "Login successful"
    else:
        return "Login failed"


