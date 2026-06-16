# Broken Access Control (CWE-284)
function getAdminPanelData(request):
    user = Session.getUser()

    data = Database.getAdminData()

    # Vulnerable: no role or permission check
    return data
