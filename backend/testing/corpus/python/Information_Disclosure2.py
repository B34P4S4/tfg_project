# Information Disclosure (CWE-200)
function getDebugInfo():
    config = {
        "db_password": "secret123",
        "api_key": "ABC-XYZ-SECRET",
        "internal_ip": "10.0.0.5"
    }

    # Vulnerable: exposes sensitive internal configuration
    return config
