
# Operaciones matemáticas básicas sin entrada externa

def sumar(a: int, b: int) -> int:
    return a + b

def dividir(a: int, b: int) -> float:
    return a / b

def mostrar_resultados():
    resultado_suma = sumar(7, 3)
    resultado_division = dividir(10, 2)

    print("Resultado suma:", resultado_suma)
    print("Resultado división:", resultado_division)

if __name__ == "__main__":
    mostrar_resultados()





