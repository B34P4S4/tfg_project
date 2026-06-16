
# Insecure Deserialization (CWE-502)
function loadObject(serializedData):
    # Vulnerable: deserializa datos sin validación ni firma
    obj = Serializer.deserialize(serializedData)
    return obj

