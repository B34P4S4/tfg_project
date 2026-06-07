# METRICAS PROPIAS DE ATAQUES Y CORRELACIONES


# ---------------------------------------------------------
# COBERTURA DE ATAQUES
# patrones activados/patrones existentes en la correlation base

def get_cobertura(
    attack_predictions,
    total_patterns
):

    if total_patterns == 0:
        return 0.0

    return (
        len(attack_predictions)
        / total_patterns
    )


# ---------------------------------------------------------
# COMPLETITUD MEDIA DE LOS PATRONES
# media de accuracy_attack

def get_media_patrones(
    attack_predictions
):

    if not attack_predictions:
        return 0.0

    values = [
        attack["accuracy_attack"]
        for attack in attack_predictions
    ]

    return (
        sum(values)
        / len(values)
    )


# ---------------------------------------------------------
# COMPLETITUD MAXIMA DE PATRON

def get_max_patrones(
    attack_predictions
):

    if not attack_predictions:
        return 0.0

    return max(
        attack["accuracy_attack"]
        for attack in attack_predictions
    )


# ---------------------------------------------------------
# FUERZA DE CORRELACION
# equivalente a la completitud media

def get_fuerza_correlacion(
    attack_predictions
):

    return (
        get_media_patrones(
            attack_predictions
        )
    )


# ---------------------------------------------------------
# DENSIDAD DE CORRELACION
# vulnerabilidades involucradas en ataques/vulnerabilidades detectadas

def get_densidad_correlacion(
    attack_predictions,
    total_detected_vulnerabilities
):

    if total_detected_vulnerabilities == 0:
        return 0.0

    correlated_vulns = set()

    for attack in attack_predictions:

        for vuln in attack[
            "vulnerabilidades_involucradas"
        ]:

            correlated_vulns.add(
                (
                    vuln["file"],
                    vuln["chunk_id"],
                    vuln["cwe"]
                )
            )

    return (
        len(correlated_vulns)
        / total_detected_vulnerabilities
    )


# ---------------------------------------------------------
# DIVERSIDAD DE ATAQUES
# numero de ataques resultantes distintos

def get_diversidad_ataque(
    attack_predictions
):

    return len({
        attack["ataque_resultante"]
        for attack in attack_predictions
    })


# ---------------------------------------------------------
# SEVERIDAD MEDIA DE ATAQUES
# CVSS medio de las vulnerabilidades involucradas en ataques

def get_severidad_ataque(
    attack_predictions
):

    scores = []

    for attack in attack_predictions:

        for vuln in attack[
            "vulnerabilidades_involucradas"
        ]:

            scores.append(
                vuln["cvss"]
            )

    if not scores:
        return 0.0

    return (
        sum(scores)
        / len(scores)
    )


# ---------------------------------------------------------
# FUNCION PRINCIPAL

def get_metricas_ataques(
    ataques_correlacionados,
    total_patrones_ataque,
    total_vulnerabilidades_detectadas
):

    ataques = ataques_correlacionados

    cobertura = (
        get_cobertura(
            ataques,
            total_patrones_ataque
        )
    )

    media_patron_completado = (
        get_media_patrones(
            ataques
        )
    )

    maximo_patron_completado = (
        get_max_patrones(
            ataques
        )
    )

    fuerza_correlacion = (
        get_fuerza_correlacion(
            ataques
        )
    )

    densidad_correlacion = (
        get_densidad_correlacion(
            ataques,
            total_vulnerabilidades_detectadas
        )
    )

    diversidad_ataques = (
        get_diversidad_ataque(
            ataques
        )
    )

    severidad_ataques = (
        get_severidad_ataque(
            ataques
        )
    )

    return {

        "Cobertura de ataque (%)":
            round(
                cobertura * 100,
                2
            ),

        "Media de patrón de ataque completado (%)":
            round(
                media_patron_completado * 100,
                2
            ),

        "Máximo número de patrón de ataque completado (%)":
            round(
                maximo_patron_completado * 100,
                2
            ),

        "Fuerza de la correlación de ataques (%)":
            round(
                fuerza_correlacion * 100,
                2
            ),

        "Densidad en la correlación de ataques (%)":
            round(
                densidad_correlacion * 100,
                2
            ),

        "Diversidad de ataques":
            diversidad_ataques,

        "Nivel de severidad de ataques":
            round(
                severidad_ataques,
                2
            )
    }