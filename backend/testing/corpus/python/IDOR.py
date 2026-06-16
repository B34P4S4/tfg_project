# Broken Access Control (IDOR) (CWE-284)
function getInvoice(request):
    user = Session.getUser()
    invoiceId = request.getParameter("invoiceId")

    invoice = Database.findInvoiceById(invoiceId)

    # Vulnerable: no check if invoice belongs to the authenticated user
    return invoice


