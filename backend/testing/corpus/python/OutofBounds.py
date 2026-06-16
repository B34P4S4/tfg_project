# Out-of-Bounds Read (CWE-126)
function readArrayValue(index):
    data = [10, 20, 30, 40, 50]

    # Vulnerable: acceso sin comprobar límites del array
    value = data[index]

    return value

