// JAVASCRIP CON LAS FUNCIONES DEL FRONTEND

const API = "http://127.0.0.1:5000/analiza"
const btn = document.getElementById("btnAnalizar")
let cy = null
btn.addEventListener("click", analizar)

const btnExportar = document.getElementById("btnExportar")
let ultimoResultado = null
btnExportar.addEventListener("click", exportarPDF)


// TABS
document.querySelectorAll(".tab").forEach(tab => {

    tab.addEventListener("click", () => {

        document.querySelectorAll(".tab")
            .forEach(t => t.classList.remove("active"))

        document.querySelectorAll(".tab-content")
            .forEach(c => c.classList.remove("active"))

        tab.classList.add("active")

        document
            .getElementById(tab.dataset.tab)
            .classList.add("active")

        // FIX CYTOSCAPE
        if (tab.dataset.tab === "correlaciones" && cy) {

            setTimeout(() => {

                cy.resize()
                cy.fit()

            }, 100)
        }
    })
})

async function exportarPDF() {

    if (!ultimoResultado) {
        alert("No hay resultados")
        return
    }

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/exportar",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(ultimoResultado)
            }
        )

        if (!response.ok) {

            const err = await response.json()
            console.error(err)

            alert(err.error || "Error exportando PDF")
            return
        }

        const blob = await response.blob()

        const url = window.URL.createObjectURL(blob)

        const a = document.createElement("a")

        a.href = url
        //a.download = "VucanAI_Report.pdf"
        document.body.appendChild(a)
        a.click()
        a.remove()
        window.URL.revokeObjectURL(url)

    } catch(e) {

        console.error(e)
        alert("Error exportando PDF")
    }
}

async function analizar() {

    const ruta = document.getElementById("ruta").value.trim()

    const loading = document.getElementById("loading")
    const dashboard = document.getElementById("dashboard")
    const errorBox = document.getElementById("errorBox")

    errorBox.classList.add("hidden")

    if (!ruta) {

        errorBox.innerText = "Error, falta ruta al proyecto"
        errorBox.classList.remove("hidden")

        return
    }

    btn.disabled = true

    loading.classList.remove("hidden")
    dashboard.classList.add("hidden")
    btnExportar.classList.add("hidden")

    try {

        const response = await fetch(API, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                path: ruta
            })
        })

        const data = await response.json()

        if (data.error) {

            errorBox.innerText = data.error
            errorBox.classList.remove("hidden")
            btnExportar.classList.add("hidden")
            return
        }

        dashboard.classList.remove("hidden")
        renderVulnerabilidades(data.vulnerabilidades)
        renderAtaques(data.ataques)
        console.log("ataques correlados:", data.ataques.ataques_detectados)
        
        setTimeout(() => {
            renderGrafico(data.ataques.ataques_detectados)
        }, 50)

        loading.classList.add("hidden")

        // BOTON EXPORTAR
        ultimoResultado = data
        btnExportar.classList.remove("hidden")
        btnExportar.disabled = false       

    }

    catch (e) {

        console.error("ERROR REAL:", e)
        errorBox.innerText = e.message || "Error conectando con backend"
        errorBox.classList.remove("hidden")
        btnExportar.classList.add("hidden")
    }

    finally {

        loading.classList.add("hidden")
        btn.disabled = false
    }
}

function getSeverityClass(cvss) {

    if (cvss >= 9) {
        return "card-critical"
    }

    if (cvss >= 7) {
        return "card-high"
    }

    if (cvss >= 5) {
        return "card-medium"
    }

    return "card-low"
}

/******************************************* */
/* VULNERABILIDADES ***************************/
/******************************************* */

function obtenerCategoria(numero) {
  const categorias = {
    1: "A01:2025 - Broken Access Control",
    2: "A02:2025 - Security Misconfiguration",
    3: "A03:2025 - Software Supply Chain Failures",
    4: "A04:2025 - Cryptographic Failures",
    5: "A05:2025 - Injection",
    6: "A06:2025 - Insecure Design",
    7: "A07:2025 - Authentication Failures",
    8: "A08:2025 - Software or Data Integrity Failures",
    9: "A09:2025 - Security Logging and Alerting Failures",
    10: "A10:2025 - Mishandling of Exceptional Conditions"
  };

  return categorias[numero] || "Número no válido";
}

function obtenerEnlaceOWASP(numero) {
  const enlaces = {
    1: "https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/",
    2: "https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/",
    3: "https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/",
    4: "https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/",
    5: "https://owasp.org/Top10/2025/A05_2025-Injection/",
    6: "https://owasp.org/Top10/2025/A06_2025-Insecure_Design/",
    7: "https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/",
    8: "https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/",
    9: "https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/",
    10: "https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/"
  };

  return enlaces[numero] || "https://owasp.org/Top10/2025/";
}

function obtenerEnlaceCWE(cwe){
    if (!cwe) {
        return "";
    }else{
        return `https://cwe.mitre.org/data/definitions/${cwe}.html`;
    }    
}

function convertirMitreLinks(texto) {

    // Técnica
    texto = texto.replace(
        /(T\d{4})\s+([^:]+?)(?=\s*:|$)/g,
        (_, tecnica, descripcion) => {

            return `
                <a href="https://attack.mitre.org/techniques/${tecnica}/" target="_blank">
                    ${tecnica}
                </a>
                ${descripcion.trim()}
            `
        }
    )

    // Táctica
    texto = texto.replace(
        /(TA\d{4})\s+(.+)$/g,
        (_, tactica, descripcion) => {

            return `
                <a href="https://attack.mitre.org/tactics/${tactica}/" target="_blank">
                    ${tactica}
                </a>
                ${descripcion.trim()}
            `
        }
    )

    return texto
}

function renderVulnerabilidades(vulnerabilidades) {

    const container = document.getElementById("vulnerabilidades")

    if (!vulnerabilidades || vulnerabilidades.length === 0) {

        container.innerHTML = `
            <div class="empty">
                No se detectaron vulnerabilidades
            </div>
        `
        return
    }

    container.innerHTML = vulnerabilidades.map(v => {

        const cvss = Number(v.cvss || 0)

        let severity = "card-low"

        if (cvss >= 9) severity = "card-critical"
        else if (cvss >= 7) severity = "card-high"
        else if (cvss >= 4) severity = "card-medium"

        const cvss_string = severity.replace("card-", "").toUpperCase();

        const mitre = Array.isArray(v.mitre)
            ? v.mitre.map(m => `<li>${convertirMitreLinks(m)}</li>`).join("")
            : "<li>N/A</li>"

        const capecs = Array.isArray(v.capecs)
            ? v.capecs.map(c => `<a href="https://capec.mitre.org/data/definitions/${c}.html" target="_blank">${c}</a>`).join(",")
            : v.capec ? `<a href="https://capec.mitre.org/data/definitions/${v.capec}.html" target="_blank">${v.capec}</a>`: "N/A";

        const enlace_owasp = obtenerEnlaceOWASP(v.owasp)
        const owasp = obtenerCategoria(v.owasp)

        const enlace_cwe = obtenerEnlaceCWE(v.cwe)

        return `

        <div class="card vuln-card ${severity}">

            <!-- RESUMEN -->
            <div class="card-header">

                <div class="vuln-title">
                    ${v.vulnerability || "N/A"}
                </div>

                <div class="vuln-meta">
                    <a href="${enlace_cwe}" target="_blank">CWE-${v.cwe || "N/A"}</a> |
                    CVSS ${v.cvss || "N/A"}/10 ${cvss_string}
                </div>

                <div class="vuln-file">
                    Archivo: ${v.file || "N/A"}
                </div>

                <div class="vuln-flow">
                    <span class="flow-label">Desde la línea:</span>
                    ${v.source || "N/A"}

                    <span class="flow-arrow">→</span>

                    <span class="flow-label">hasta la línea:</span>
                    ${v.sink || "N/A"}
                </div>

            </div>

            <!-- DETALLES -->
            <details class="details-box">

                <summary>
                    Detalles
                </summary>

                <div class="details-content">

                    <p>
                        <strong>Descripción:</strong>
                        ${v.description || "N/A"}
                    </p>

                    <p>
                        <strong>Impacto:</strong>
                        ${v.impact || "N/A"}/5
                        &nbsp; | &nbsp;
                        <strong>Probabilidad:</strong>
                        ${v.probability || "N/A"}/5
                    </p>

                    <p>
                        <strong>OWASP:</strong>
                        <a href="${enlace_owasp}" target="_blank">${owasp}</a>
                    </p>

                    <p>
                        <strong>CAPEC:</strong>
                        ${capecs}
                    </p>

                    <div class="mitre-section">

                        <strong>MITRE ATT&CK:</strong>

                        <ul>
                            ${mitre}
                        </ul>

                    </div>

                </div>

            </details>

        </div>
        `
    }).join("")
}

function renderAtaques(ataquesData) {

    const ataques = ataquesData.ataques_detectados

    const div = document.getElementById("ataques")

    if (!ataques || ataques.length === 0) {

        div.innerHTML = `
            <div class="empty">
                No se detectaron correlaciones de ataque
            </div>
        `
        return
    }

    div.innerHTML = ataques.map(a => {

        const accuracy_value = (a.accuracy_attack || 0) * 100

        let accuracy = "card-low"

        if (accuracy_value >= 90) {
            accuracy = "card-critical"
        }
        else if (accuracy_value >= 60) {
            accuracy = "card-high"
        }
        else if (accuracy_value >= 40) {
            accuracy = "card-medium"
        }

        const accuracy_attack = Math.round(accuracy_value * 100) / 100

        const capecs = Array.isArray(a.capec)
            ? a.capec.map(c => `<a href="https://capec.mitre.org/data/definitions/${c.id}.html" target="_blank">${c.id}</a>`).join(",")
            : (a.capec || "N/A")
        
        

        return `
        <div class="card attack-card ${accuracy}">

            <div class="card-header">

                <div>
                    <div class="card-title">
                        ${a.nombre}
                    </div>

                    <div class="card-subtitle">
                        Precisión: ${accuracy_attack}%  
                    </div>
                </div>

            </div>

            <div class="attack-result">
                ${a.ataque_resultante}
            </div>

            <details>

                <summary>Detalles</summary>

                <div class="details-content">

                    <p>
                        <strong>Descripción:</strong>
                        ${a.descripcion}
                    </p>

                    <p>
                        <strong>CAPECs:</strong>
                        ${capecs}
                    </p>

                    <p>
                        <strong>Vulnerabilidades correlacionadas:</strong>
                    </p>

                    <ul>
                        ${(a.vulnerabilidades_involucradas || []).map(v => `
                            <li>
                                ${v.vulnerability} (<a href="${obtenerEnlaceCWE(v.cwe)}" target="_blank">CWE-${v.cwe || "N/A"}</a>) <span class="flow-arrow">→</span> Ruta:${v.file}
                            </li>
                        `).join("")}
                    </ul>

                </div>

            </details>

        </div>
        `
    }).join("")
}

// funcion para el dibujo de red de correlacion entre vulnerabilidades propinando ataques
function renderGrafico(ataques) {

    const elements = []

    ataques.forEach((ataque, attackIndex) => {

        const attackId = `attack_${attackIndex}`

        const accuracy = (ataque.accuracy_attack || 0) * 100

        // COLOR SEGÚN EXACTITUD
        let attackColor = "#22c55e"

        if (accuracy >= 80) {
            attackColor = "#dc2626"
        }
        else if (accuracy >= 50) {
            attackColor = "#f59e0b"
        }

        // NODO ATAQUE
        elements.push({

            data: {

                id: attackId,
                label: ataque.nombre,
                type: "attack",
                color: attackColor,
                accuracy: accuracy,
                capec: ataque.capec,
                descripcion: ataque.descripcion,
                resultado: ataque.ataque_resultante
            }
        })

        // VULNERABILIDADES
        ataque.vulnerabilidades_involucradas.forEach((vuln, vulnIndex) => {

            const vulnId = `v_${vuln.cwe}_${attackIndex}_${vulnIndex}`

            const cvss = vuln.cvss || 5

            const size = 30 + (cvss * 4)

            elements.push({

                data: {

                    id: vulnId,

                    label: vuln.vulnerability,

                    type: "vulnerability",

                    cvss: cvss,

                    cwe: vuln.cwe,

                    impact: vuln.impact,

                    probability: vuln.probability,

                    file: vuln.file,

                    size: size
                }
            })

            // RELACIÓN
            elements.push({

                data: {

                    source: vulnId,

                    target: attackId
                }
            })
        })
    })

    cy = cytoscape({

        container: document.getElementById("correlationGraph"),

        elements: elements,

        style: [

            // VULNERABILIDADES
            {
                selector: 'node[type="vulnerability"]',

                style: {

                    'background-color': '#2563eb',

                    'label': 'data(label)',

                    'color': 'white',

                    'font-size': '10px',

                    'text-wrap': 'wrap',

                    'text-max-width': '80px',

                    'text-valign': 'center',

                    'text-halign': 'center',

                    'width': 'data(size)',

                    'height': 'data(size)',

                    'border-width': 2,

                    'border-color': '#60a5fa'
                }
            },

            // ATAQUES
            {
                selector: 'node[type="attack"]',

                style: {

                    'background-color': 'data(color)',

                    'label': 'data(label)',

                    'shape': 'diamond',

                    'color': 'white',

                    'font-size': '12px',

                    'font-weight': 'bold',

                    'text-wrap': 'wrap',

                    'text-max-width': '120px',

                    'text-valign': 'center',

                    'text-halign': 'center',

                    'width': 90,

                    'height': 90,

                    'border-width': 3,

                    'border-color': '#ffffff'
                }
            },

            // ARISTAS
            {
                selector: 'edge',

                style: {

                    'width': 2,

                    'line-color': '#64748b',

                    'target-arrow-color': '#64748b',

                    'target-arrow-shape': 'triangle',

                    'curve-style': 'bezier',

                    'opacity': 0.8
                }
            }
        ],

        layout: {

            name: 'cose',

            animate: true,

            nodeRepulsion: 800000,

            idealEdgeLength: 150,

            gravity: 0.25
        }
    })

    // CLICK EN NODOS
    cy.on('tap', 'node', function(evt) {

        const data = evt.target.data()

        const details = document.getElementById("detailsContent")

        const capecs_detail = Array.isArray(data.capec)
            ? data.capec.map(c => `<a href="https://capec.mitre.org/data/definitions/${c.id}.html" target="_blank">${c.id}</a>`).join(",")
            : (data.capec || "N/A")

        if (data.type === "attack") {

            details.innerHTML = `

                <h4>${data.label}</h4>
                <p><b>Resultado:</b> ${data.resultado}</p>
                <p><b>Precisión:</b> ${data.accuracy}%</p>
                <p><b>CAPEC:</b> ${capecs_detail}</p>
                <p><b>Descripción:</b> ${data.descripcion}</p>
            `
        }

        else {

            details.innerHTML = `

                <h4>${data.label}</h4>
                <p><b>CWE:</b> ${data.cwe}</p>
                <p><b>CVSS:</b> ${data.cvss}</p>
                <p><b>Impacto:</b> ${data.impact}/5</p>
                <p><b>Probabilidad:</b> ${data.probability}/5</p>
                <p><b>Ruta:</b> ${data.file}</p>
            `
        }
    })

    // HOVER EFFECT
    cy.on('mouseover', 'node', function(e) {

        e.target.style('border-color', '#ffffff')
        e.target.style('border-width', '5px')
    })

    cy.on('mouseout', 'node', function(e) {

        e.target.style('border-width', '2px')
    })
}