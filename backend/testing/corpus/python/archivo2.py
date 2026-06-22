

# Manejo de datos internos sin interacción externa

libros = [
    {"id": 1, "titulo": "Python Básico"},
    {"id": 2, "titulo": "Seguridad Informática"},
    {"id": 3, "titulo": "Redes"}
]

def listar_libros():
    for libro in libros:
        print(f"ID: {libro['id']} | Título: {libro['titulo']}")

def contar_libros() -> int:
    return len(libros)

if __name__ == "__main__":
    listar_libros()
    print("Total de libros:", contar_libros())






