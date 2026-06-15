# OBTENCION DE ESTADISTICAS GLOBALES DE LOS ANALISIS ALMACENADOS EN EL HISTORICO
import sqlite3
import json
from collections import defaultdict, Counter
from pathlib import Path

from backend.storage.database import conectar_bd


def get_estadisticas_globales():

    conn = conectar_bd()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:

        stats = {}

        # =====================================================
        # ANALISIS
        # =====================================================

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM analisis
        """)
        stats["total_analisis"] = cursor.fetchone()["total"]

        # =====================================================
        # VULNERABILIDADES
        # =====================================================

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM vulnerabilidades
        """)
        stats["total_vulnerabilidades"] = cursor.fetchone()["total"]

        # =====================================================
        # VULNERABILIDADES POR TIPO
        # =====================================================

        cursor.execute("""
            SELECT
                vulnerabilidad,
                COUNT(*) AS total
            FROM vulnerabilidades
            GROUP BY vulnerabilidad
            ORDER BY total DESC
        """)

        stats["detecciones_por_vulnerabilidad"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # CWE MAS FRECUENTES
        # =====================================================

        cursor.execute("""
            SELECT
                cwe,
                COUNT(*) AS total
            FROM vulnerabilidades
            WHERE cwe IS NOT NULL
            GROUP BY cwe
            ORDER BY total DESC
        """)

        stats["cwe_mas_frecuentes"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # NUMERO DE CWE DISTINTOS
        # =====================================================

        cursor.execute("""
            SELECT COUNT(DISTINCT cwe) AS total
            FROM vulnerabilidades
            WHERE cwe IS NOT NULL
        """)

        stats["total_cwe_distintos"] = cursor.fetchone()["total"]

        # =====================================================
        # OWASP MAS FRECUENTES
        # =====================================================

        cursor.execute("""
            SELECT
                owasp,
                COUNT(*) AS total
            FROM vulnerabilidades
            WHERE owasp IS NOT NULL
            GROUP BY owasp
            ORDER BY total DESC
        """)

        stats["owasp_mas_frecuentes"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # ATAQUES
        # =====================================================

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM ataques
        """)
        stats["total_ataques"] = cursor.fetchone()["total"]

        cursor.execute("PRAGMA table_info(ataques)")
        print("INFORMACION TABLA ATAQUES")
        for row in cursor.fetchall():
            print(dict(row))

        # =====================================================
        # ATAQUES POR TIPO
        # =====================================================

        cursor.execute("""
            SELECT
                nombre,
                COUNT(*) AS total
            FROM ataques
            GROUP BY nombre
            ORDER BY total DESC
        """)

        stats["ataques_por_tipo"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # CAPEC MAS FRECUENTES
        # =====================================================

        cursor.execute("""
            SELECT capec
            FROM ataques
            WHERE capec IS NOT NULL
        """)

        contador = Counter()

        for row in cursor.fetchall():

            try:

                capecs = json.loads(row["capec"])

                if isinstance(capecs, list):

                    for capec in capecs:

                        capec_id = capec.get("id")

                        if capec_id:
                            contador[capec_id] += 1

            except Exception:
                pass

        stats["capec_mas_frecuentes"] = [
            {
                "capec": capec,
                "total": total
            }
            for capec, total in contador.most_common()
        ]

        # =====================================================
        # NUMERO DE CAPEC DISTINTOS
        # =====================================================

        cursor.execute("""
            SELECT COUNT(DISTINCT capec) AS total
            FROM ataques
            WHERE capec IS NOT NULL
        """)

        stats["total_capec_distintos"] = cursor.fetchone()["total"]

        # =====================================================
        # PRECISION MEDIA GLOBAL
        # =====================================================

        cursor.execute("""
            SELECT AVG(precision) AS media
            FROM ataques
            WHERE precision IS NOT NULL
        """)

        row = cursor.fetchone()

        stats["precision_media_global"] = round(
            row["media"], 2
        ) if row["media"] is not None else 0

        # =====================================================
        # SEVERIDAD CVSS
        # =====================================================

        cursor.execute("""
            SELECT cvss
            FROM vulnerabilidades
            WHERE cvss IS NOT NULL
        """)

        criticas = 0
        altas = 0
        medias = 0
        bajas = 0

        for row in cursor.fetchall():

            try:
                cvss = float(row["cvss"])
            except (TypeError, ValueError):
                continue

            if cvss >= 9.0:
                criticas += 1

            elif cvss >= 7.0:
                altas += 1

            elif cvss >= 4.0:
                medias += 1

            else:
                bajas += 1

        stats["severidad"] = {
            "criticas": criticas,
            "altas": altas,
            "medias": medias,
            "bajas": bajas
        }

        # =====================================================
        # PORCENTAJE DE CRITICAS
        # =====================================================

        total_vulns = stats["total_vulnerabilidades"]

        stats["porcentaje_criticas"] = round(
            (criticas / total_vulns) * 100,
            2
        ) if total_vulns else 0

        # =====================================================
        # VULNERABILIDADES POR IMPACTO
        # =====================================================

        cursor.execute("""
            SELECT
                impacto,
                COUNT(*) AS total
            FROM vulnerabilidades
            WHERE impacto IS NOT NULL
            GROUP BY impacto
            ORDER BY impacto DESC
        """)

        stats["vulnerabilidades_por_impacto"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # VULNERABILIDADES POR PROBABILIDAD
        # =====================================================

        cursor.execute("""
            SELECT
                probabilidad,
                COUNT(*) AS total
            FROM vulnerabilidades
            WHERE probabilidad IS NOT NULL
            GROUP BY probabilidad
            ORDER BY probabilidad DESC
        """)

        stats["vulnerabilidades_por_probabilidad"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # VULNERABILIDADES POR LENGUAJE
        # =====================================================

        cursor.execute("""
            SELECT ruta
            FROM vulnerabilidades
            WHERE ruta IS NOT NULL
        """)

        extensiones = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".php": "PHP",
            ".sql": "SQL"
        }

        lenguaje_stats = defaultdict(int)

        for row in cursor.fetchall():

            ruta = row["ruta"]

            extension = Path(ruta).suffix.lower()

            lenguaje = extensiones.get(extension)

            if lenguaje:
                lenguaje_stats[lenguaje] += 1

        stats["vulnerabilidades_por_lenguaje"] = dict(lenguaje_stats)

        # =====================================================
        # ANALISIS MAS VULNERABLES
        # =====================================================

        cursor.execute("""
            SELECT
                a.id,
                a.ruta_proyecto,
                COUNT(v.id) AS total_vulnerabilidades
            FROM analisis a
            LEFT JOIN vulnerabilidades v
                ON a.id = v.analisis_id
            GROUP BY a.id
            ORDER BY total_vulnerabilidades DESC
            LIMIT 10
        """)

        stats["top_analisis_vulnerables"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # PROYECTOS MAS VULNERABLES
        # =====================================================

        cursor.execute("""
            SELECT
                ruta_proyecto,
                SUM(total_vulnerabilidades) AS vulnerabilidades,
                SUM(total_ataques) AS ataques,
                COUNT(*) AS veces_analizado
            FROM analisis
            GROUP BY ruta_proyecto
            ORDER BY vulnerabilidades DESC
            LIMIT 20
        """)

        stats["proyectos_mas_vulnerables"] = [
            dict(row) for row in cursor.fetchall()
        ]

        # =====================================================
        # CORRELACIONES
        # =====================================================

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM correlaciones
        """)

        stats["total_correlaciones"] = cursor.fetchone()["total"]

        # =====================================================
        # RATIO CORRELACIONES / VULNERABILIDADES
        # =====================================================

        stats["ratio_correlacion_vulnerabilidades"] = round(
            stats["total_correlaciones"] / stats["total_vulnerabilidades"],
            2
        ) if stats["total_vulnerabilidades"] else 0

        # =====================================================
        # MEDIA DE VULNERABILIDADES POR ANALISIS
        # =====================================================

        stats["media_vulnerabilidades_por_analisis"] = round(
            stats["total_vulnerabilidades"] / stats["total_analisis"],
            2
        ) if stats["total_analisis"] else 0

        # =====================================================
        # MEDIA DE ATAQUES POR ANALISIS
        # =====================================================

        stats["media_ataques_por_analisis"] = round(
            stats["total_ataques"] / stats["total_analisis"],
            2
        ) if stats["total_analisis"] else 0

        # =====================================================
        # HISTORICO DE ANALISIS
        # =====================================================

        cursor.execute("""
            SELECT
                DATE(analisis_fecha) AS fecha,
                COUNT(*) AS total_analisis,
                SUM(total_vulnerabilidades) AS vulnerabilidades,
                SUM(total_ataques) AS ataques
            FROM analisis
            GROUP BY DATE(analisis_fecha)
            ORDER BY fecha
        """)

        stats["historico"] = [
            dict(row) for row in cursor.fetchall()
        ]

        return stats

    finally:
        conn.close()