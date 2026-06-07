# GESTION DE LA INFORMACION QUE SE VA A ALMACENAR Y OBTENER DE LA BASE DE DATOS
from backend.storage.database import conectar_bd
from datetime import datetime
import json
import traceback

def guardar_analisis(path, vulnerabilidades, ataques):

    conn = conectar_bd()
    cursor = conn.cursor()

    try:
        # =========================
        # INSERT ANALISIS
        # =========================
        print("INSERTANDO ANALISIS --------------------------------")
        cursor.execute(
            """
            INSERT INTO analisis(
                ruta_proyecto,
                analisis_fecha,
                total_vulnerabilidades,
                total_ataques
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                path,
                datetime.now().isoformat(),
                len(vulnerabilidades),
                len(ataques.get("ataques_detectados", []))
            )
        )
        #print("OK ANALYSIS STORED")

        analisis_id = cursor.lastrowid

        # =========================
        # INSERT VULNERABILIDADES
        # =========================
        print("INSERTANDO VULNERABILIDADES --------------------------------")
        vuln_map = {}

        for vuln in vulnerabilidades:

            mitre = vuln.get("mitre")
            if isinstance(mitre, str):
                mitre = json.dumps([mitre])
            else:
                mitre = json.dumps(mitre)

            mitigation = vuln.get("mitigation")
            if isinstance(mitigation, str):
                mitigation = json.dumps([mitigation])
            else:
                mitigation = json.dumps(mitigation)

            valores = (
                analisis_id,
                vuln.get("vulnerability"),
                vuln.get("cwe"),
                vuln.get("cvss"),
                vuln.get("impact"),
                vuln.get("probability"),
                vuln.get("file"),
                vuln.get("chunk_id"),
                vuln.get("source"),
                vuln.get("sink"),
                vuln.get("owasp"),
                vuln.get("description"),
                mitre,
                mitigation
            )

            #print("TIPOS DE VULNERABILIDADES >>> ")
            #for i, v in enumerate(valores, start=1):
                #print(f"{i}: {type(v)} -> {repr(v)}")

            cursor.execute(
                """
                INSERT INTO vulnerabilidades (
                    analisis_id,
                    vulnerabilidad,
                    cwe,
                    cvss,
                    impacto,
                    probabilidad,
                    ruta,
                    chunk_id,
                    source,
                    sink,
                    owasp,
                    descripcion,
                    mitre,
                    mitigacion
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    analisis_id,
                    vuln.get("vulnerability"),
                    vuln.get("cwe"),
                    vuln.get("cvss"),
                    vuln.get("impact"),
                    vuln.get("probability"),
                    vuln.get("file"),
                    vuln.get("chunk_id"),
                    vuln.get("source"),
                    vuln.get("sink"),
                    vuln.get("owasp"),
                    vuln.get("description"),
                    mitre,
                    mitigation
                )
            )
            #print("OK VULNS STORED")

            vuln_id = cursor.lastrowid

            key = (
                vuln.get("chunk_id"),
                vuln.get("file"),
                vuln.get("cwe")
            )

            vuln_map[key] = vuln_id

        # =========================
        # INSERT ATAQUES
        # =========================
        print("INSERTANDO ATAQUES --------------------------------")

        for ataque in ataques.get("ataques_detectados", []):

            capec = ataque.get("capec", [])

            if isinstance(capec, (int, float)):
                capec = [{"id": int(capec)}]
            elif isinstance(capec, str):
                try:
                    capec = json.loads(capec)
                except:
                    capec = []

            cursor.execute(
                """
                INSERT INTO ataques (
                    analisis_id,
                    nombre,
                    ataque_resultante,
                    descripcion,
                    capec,
                    precision
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    analisis_id,
                    ataque.get("nombre"),
                    ataque.get("ataque_resultante"),
                    ataque.get("descripcion"),
                    json.dumps(capec),
                    ataque.get("accuracy_attack")
                )
            )
            #print("OK ATAQUES STORED")

            ataque["_db_id"] = cursor.lastrowid

        # =========================
        # INSERT CORRELACIONES
        # =========================
        print("INSERTANDO CORRELACIONES --------------------------------")

        for ataque in ataques.get("ataques_detectados", []):

            ataque_id = ataque["_db_id"]

            for vuln in ataque.get("vulnerabilidades_involucradas", []):

                key = (
                    vuln.get("chunk_id"),
                    vuln.get("file"),
                    vuln.get("cwe")
                )

                vulnerabilidad_id = vuln_map.get(key)

                if vulnerabilidad_id:

                    cursor.execute(
                        """
                        INSERT INTO correlaciones (
                            analisis_id,
                            ataque_id,
                            vulnerabilidad_id
                        )
                        VALUES (?, ?, ?)
                        """,
                        (
                            analisis_id,
                            ataque_id,
                            vulnerabilidad_id
                        )
                    )
                    #print("OK CORRELACIONES STORED")

        conn.commit()
        return analisis_id

    except Exception as e:
        conn.rollback()
        traceback.print_exc()
        raise

    finally:
        conn.close()

def obtener_vulnerabilidades(analisis_id):

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ruta,
            chunk_id,
            vulnerabilidad,
            descripcion,
            source,
            sink,
            cvss,
            impacto,
            probabilidad,
            owasp,
            cwe,
            mitre,
            mitigacion
        FROM vulnerabilidades
        WHERE analisis_id = ?
    """, (analisis_id,))

    filas = cursor.fetchall()

    conn.close()

    vulnerabilidades = []

    for row in filas:

        vulnerabilidad = {

            # No existen actualmente en la BD
            "modelo": None,
            "language": None,

            "file": row["ruta"],
            "chunk_id": row["chunk_id"],

            # VULNERABILIDAD
            "vulnerability": row["vulnerabilidad"],
            "description": row["descripcion"],

            # SOURCE / SINK
            "source": row["source"],
            "sink": row["sink"],

            # RIESGO
            "cvss": row["cvss"],
            "impact": row["impacto"],
            "probability": row["probabilidad"],

            # OWASP / CAPEC / CWE
            "owasp": row["owasp"],
            "capec": None,   # no la estás almacenando
            "cwe": row["cwe"],

            # MITRE
            "mitre": json.loads(row["mitre"])
                     if row["mitre"] else [],

            # MITIGACIÓN
            "mitigation": json.loads(row["mitigacion"])
                          if row["mitigacion"] else []
        }

        vulnerabilidades.append(vulnerabilidad)

    return vulnerabilidades

def safe_json(val):

    if val is None:
        return []

    if isinstance(val, (list, dict)):
        return val

    if isinstance(val, (int, float)):
        return [{"id": int(val)}]

    if isinstance(val, str):
        try:
            return json.loads(val)
        except:
            return []

    return []

def obtener_ataques(analisis_id):

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            nombre,
            ataque_resultante,
            descripcion,
            capec,
            precision
        FROM ataques
        WHERE analisis_id = ?
    """, (analisis_id,))

    ataques_bd = cursor.fetchall()

    ataques = []

    for ataque in ataques_bd:

        ataque_id = ataque["id"]

        # Obtener vulnerabilidades correlacionadas
        cursor.execute("""
            SELECT
                v.id,
                v.vulnerabilidad,
                v.cwe,
                v.ruta,
                v.chunk_id,
                v.cvss,
                v.impacto,
                v.probabilidad,
                v.descripcion
            FROM correlaciones c
            INNER JOIN vulnerabilidades v
                ON c.vulnerabilidad_id = v.id
            WHERE c.analisis_id = ?
              AND c.ataque_id = ?
        """, (analisis_id, ataque_id))

        vulnerabilidades = []

        for vuln in cursor.fetchall():

            vulnerabilidades.append({

                "id": vuln["id"],
                "file": vuln["ruta"],
                "chunk_id": vuln["chunk_id"],

                "vulnerability": vuln["vulnerabilidad"],
                "description": vuln["descripcion"],

                "cwe": vuln["cwe"],
                "cvss": vuln["cvss"],
                "impact": vuln["impacto"],
                "probability": vuln["probabilidad"]
            })
        
       
        ataques.append({
            "id": ataque_id,
            "nombre": ataque["nombre"],
            "ataque_resultante": ataque["ataque_resultante"],
            "descripcion": ataque["descripcion"],
            "capec": safe_json(ataque["capec"]),
            "accuracy_attack": ataque["precision"],
            "vulnerabilidades_involucradas": vulnerabilidades
        })

    conn.close()

    return ataques

def obtener_analisis(analisis_id):

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            ruta_proyecto,
            analisis_fecha,
            total_vulnerabilidades,
            total_ataques
        FROM analisis
        WHERE id = ?
    """, (analisis_id,))

    row = cursor.fetchone()

    if not row:
        return None

    return {
        "id": row["id"],
        "ruta_proyecto": row["ruta_proyecto"],
        "analisis_fecha": row["analisis_fecha"],
        "total_vulnerabilidades": row["total_vulnerabilidades"],
        "total_ataques": row["total_ataques"],

        # 
        "vulnerabilidades": obtener_vulnerabilidades(analisis_id),
        "ataques": obtener_ataques(analisis_id)
    }

def obtener_ultimos_analisis(limit=20):

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            analisis_fecha,
            total_vulnerabilidades,
            total_ataques,
            ruta_proyecto
        FROM analisis
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": r[0],
            "fecha": r[1],
            "total_vulnerabilidades": r[2],
            "total_ataques": r[3],
            "ruta": r[4]
        }
        for r in rows
    ]