# Cross-Site Request Forgery (CWE-352)
function updateEmail(request):
    user = Session.getUser()

    newEmail = request.getParameter("email")

    # Vulnerable: no CSRF token validation
    Database.updateUserEmail(user.id, newEmail)

    return "Email updated"


