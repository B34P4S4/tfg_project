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

    # VAMOS A CALCULAR LA VERACIDAD DE LA RESPUESTA DE LA IA COMPARANDOLA CON NUESTRA BASE DE CONOCIMIENTO CONTRASTADA
    # EL NIVEL DE EXACTITUD ADECUADO DEBE SER >= 80%, SI ES MENOR SE CONSIDERA INEXACTO DEBIDO A ALUCINACIONES DE LA IA
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

# AÑADIR ACCURACY_SCORE A CADA VULNERABILIDAD CON EL NIVEL DE EXACTITUD SEGUN SE PAREZCA MÁS AL RAG
def calcular_accuracy(vulns):

    resultado = []

    for vuln in vulns:

        referencia = buscar_referencia(vuln)

        vuln_con_score = vuln.copy()

        if referencia:

            vuln_con_score["accuracy_score"] = calcular_score(
                vuln,
                referencia
            )

        else:

            print(
                f"[WARNING] No se encontró referencia CWE "
                f"{vuln.get('cwe')}"
            )

            vuln_con_score["accuracy_score"] = 0

        resultado.append(vuln_con_score)

    return resultado

# DEDUPLICACIÓN CON ELECCIÓN DEL MEJOR MODELO SEGUN ACCURACY_SCORE CALCULADO
def deduplicar(vulns):

    grupos = {}

    for vuln in vulns:

        key = (
            vuln.get("file"),
            vuln.get("chunk_id"),
            vuln.get("cwe")
        )

        grupos.setdefault(key, []).append(vuln)

    resultado_final = []

    for key, grupo in grupos.items():

        print("COMPARANDO VULNERABILIDADES")
        print("====================================")

        mejor_vuln = max(
            grupo,
            key=lambda v: v.get("accuracy_score", 0)
        )

        for vuln in grupo:

            print(
                f"Modelo: {vuln.get('modelo')} | "
                f"Vuln: {vuln.get('vulnerability')} | "
                f"CWE: {vuln.get('cwe')} | "
                f"Score exactitud: {vuln.get('accuracy_score', 0)}"
            )

        resultado_final.append(mejor_vuln)

    return resultado_final


'''def deduplicar(vulns):

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

    return resultado_final'''