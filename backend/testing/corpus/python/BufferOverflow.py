# Buffer Overflow (CWE-120)
function processInput(userInput):
    buffer = new char[16]

    # Vulnerable: no check on input size
    for i from 0 to length(userInput):
        buffer[i] = userInput[i]

    return buffer




