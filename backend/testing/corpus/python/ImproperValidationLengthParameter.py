# Improper Validation of Length Parameter (CWE-130)
function copyUserInput(input, length):
    buffer = new char[10]

    # Vulnerable: no valida si length excede el tamaño del buffer
    for i from 0 to length:
        buffer[i] = input[i]

    return buffer


