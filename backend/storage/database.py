#GESTION DE LA BASE DE DATOS
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "vucanAI_bd.db"

def conectar_bd():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def crear_bd():

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS analisis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ruta_proyecto TEXT NOT NULL,
        analisis_fecha DATETIME NOT NULL,
        total_vulnerabilidades INTEGER,
        total_ataques INTEGER
    );

    CREATE TABLE IF NOT EXISTS vulnerabilidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analisis_id INTEGER NOT NULL,
        vulnerabilidad TEXT,
        cwe INTEGER,
        cvss REAL,
        impacto INTEGER,
        probabilidad INTEGER,
        ruta TEXT,
        chunk_id INTEGER,
        source INTEGER,
        sink INTEGER,
        owasp INTEGER,
        descripcion TEXT,
        mitre TEXT,
        mitigacion TEXT,
        UNIQUE (
            analisis_id,
            chunk_id,
            ruta,
            cwe
        ),                       
        FOREIGN KEY (analisis_id)
            REFERENCES analisis(id)
    );

    CREATE TABLE IF NOT EXISTS ataques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analisis_id INTEGER,
        nombre TEXT,
        ataque_resultante TEXT,
        descripcion TEXT,
        capec INTEGER,
        precision REAL,                         
        FOREIGN KEY (analisis_id)
            REFERENCES analisis(id)
    );
                         
    CREATE TABLE IF NOT EXISTS correlaciones (
        analisis_id INTEGER NOT NULL,
        ataque_id INTEGER NOT NULL,
        vulnerabilidad_id INTEGER NOT NULL,

        PRIMARY KEY (
            analisis_id,
            ataque_id,
            vulnerabilidad_id
        ),

        FOREIGN KEY (analisis_id)
            REFERENCES analisis(id),

        FOREIGN KEY (ataque_id)
            REFERENCES ataques(id),

        FOREIGN KEY (vulnerabilidad_id)
            REFERENCES vulnerabilidades(id)
    );
    """)

    conn.commit()
    conn.close()

def borrar_bd():
    """
    Elimina completamente la estructura de la base de datos.
    """
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS correlaciones;
    DROP TABLE IF EXISTS ataques;
    DROP TABLE IF EXISTS vulnerabilidades;
    DROP TABLE IF EXISTS analisis;
    """)

    conn.commit()
    conn.close()

def reiniciar_bd():
    borrar_bd()
    crear_bd()

