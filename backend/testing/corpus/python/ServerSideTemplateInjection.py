# Server-Side Template Injection (CWE-1336)
function renderTemplate(userInput):
    template = "Hello " + userInput

    # Vulnerable: el input del usuario se interpreta como plantilla
    output = TemplateEngine.render(template)
    return output

