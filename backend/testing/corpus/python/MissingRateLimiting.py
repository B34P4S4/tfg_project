# Missing Rate Limiting (CWE-770)
function sendVerificationCode(request):
    email = request.getParameter("email")

    user = Database.findUserByEmail(email)

    # Vulnerable: no limit on number of requests per user/IP
    CodeService.sendCode(user.email)

    return "Verification code sent"