from backend.storage.database import conectar_bd, crear_bd, borrar_bd, reiniciar_bd
from backend.storage.repository import guardar_analisis

def test_conexion():
    conn = conectar_bd()
    print("CONEXION BASE DE DATOS:",conn)
    conn.close()

def test_crear():   
    reiniciar_bd()
    
def test_resultados_bd():
    conn = conectar_bd()    
    cursor = conn.cursor()

    print("ANALISIS")
    for row in cursor.execute("SELECT * FROM analisis"):
        print(dict(row))

    print("\nVULNERABILIDADES")
    for row in cursor.execute("SELECT * FROM vulnerabilidades"):
        print(dict(row))

    print("\nATAQUES")
    for row in cursor.execute("SELECT * FROM ataques"):
        print(dict(row))

    print("\nCORRELACIONES")
    for row in cursor.execute("SELECT * FROM correlaciones"):
        print(dict(row))

    conn.close()

