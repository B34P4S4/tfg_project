# Cross-Site Scripting (CWE-79)
function renderComment(userInput):
    html = "<div>" + userInput + "</div>"
    return html


