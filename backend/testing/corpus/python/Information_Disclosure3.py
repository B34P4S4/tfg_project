
# Information Disclosure (CWE-200)
function getUserProfile(userId):
    user = Database.find(userId)

    # Vulnerable: expone información sensible sin filtrado
    return user