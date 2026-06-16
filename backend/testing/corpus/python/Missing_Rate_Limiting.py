# Missing Rate Limiting (CWE-770)
function requestPasswordReset(email):
    user = Database.findUserByEmail(email)

    # Vulnerable: sin límite de peticiones por usuario o IP
    EmailService.sendResetLink(user.email)

    return "Reset email sent"