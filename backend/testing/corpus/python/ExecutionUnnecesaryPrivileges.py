
# Execution with Unnecessary Privileges (CWE-250)
function generateReport(data):
    # Vulnerable: ejecución con privilegios elevados innecesarios
    elevatePrivileges("admin")

    result = SystemCommand.execute("generate_report_tool " + data)

    dropPrivileges()

    return result