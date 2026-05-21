from backend.ai.rag.knowledge_base import KNOWLEDGE_BASE

# BUSCAR REFERENCIA EN KNOWLEDGE BASE
def buscar_referencia(vuln):

    cwe = vuln.get("cwe")

    for item in KNOWLEDGE_BASE:

        if item.get("3.4") == cwe:
            return item

    return None

# CALCULAR SCORE DE EXACTITUD
def calcular_score(vuln, referencia):

    score = 0

    # CWE
    if vuln.get("cwe") == referencia.get("3.4"):
        score += 50

    # OWASP
    if vuln.get("owasp") == referencia.get("3.1"):
        score += 30

    # CAPEC
    if vuln.get("capec") == referencia.get("3.2"):
        score += 15

    # CVSS
    cvss_modelo = vuln.get("cvss", 0)
    cvss_real = referencia.get("2.1", 0)

    diferencia = abs(cvss_modelo - cvss_real)
    # cuanto menor diferencia mejor
    score += max(0, 5 - diferencia)

    return score


# DEDUPLICACIÓN + ELECCIÓN DEL MEJOR MODELO
def deduplicar(vulns):

    grupos = {}

    for vuln in vulns:

        key = (
            vuln.get("file"),
            vuln.get("chunk_id"),
            vuln.get("cwe")
        )

        if key not in grupos:
            grupos[key] = []

        grupos[key].append(vuln)

    resultado_final = []
   
    # COMPARAR MODELOS
    for key, grupo in grupos.items():

        mejor_vuln = None
        mejor_score = -1

        print("COMPARANDO VULNERABILIDADES")
        print("====================================")

        for vuln in grupo:

            referencia = buscar_referencia(vuln)

            if not referencia:

                print(
                    f"[WARNING] No se encontró referencia CWE "
                    f"{vuln.get('cwe')}"
                )

                continue

            score = calcular_score(
                vuln,
                referencia
            )

            print(
                f"Modelo: {vuln.get('modelo')} | "
                f"Vuln: {vuln.get('vulnerability')} | "
                f"CWE: {vuln.get('cwe')} | "
                f"Score exactitud: {score}"
            )

            if score > mejor_score:

                mejor_score = score
                mejor_vuln = vuln

        # guardamos score final
        if mejor_vuln:

            mejor_vuln["accuracy_score"] = mejor_score
            resultado_final.append(mejor_vuln)

    return resultado_final