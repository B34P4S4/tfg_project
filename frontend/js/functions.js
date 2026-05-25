// JAVASCRIP CON LAS FUNCIONES DEL FRONTEND

const API = "http://127.0.0.1:5000/analiza"
const btn = document.getElementById("btnAnalizar")
let cy = null
btn.addEventListener("click", analizar)


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

    }

    catch (e) {

        console.error("ERROR REAL:", e)
        errorBox.innerText = e.message || "Error conectando con backend"
        errorBox.classList.remove("hidden")
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

        const mitre = Array.isArray(v.mitre)
            ? v.mitre.map(m => `<li>${m}</li>`).join("")
            : "<li>N/A</li>"

        const capecs = Array.isArray(v.capecs)
            ? v.capecs.join(", ")
            : (v.capec || "N/A")

        return `

        <div class="card vuln-card ${severity}">

            <!-- RESUMEN -->
            <div class="card-header">

                <div class="vuln-title">
                    ${v.vulnerability || "N/A"}
                </div>

                <div class="vuln-meta">
                    CWE-${v.cwe || "N/A"} |
                    CVSS ${v.cvss || "N/A"}/10
                </div>

                <div class="vuln-file">
                    Archivo: ${v.file || "N/A"}
                </div>

                <div class="vuln-flow">
                    <span class="flow-label">From:</span>
                    ${v.source || "N/A"}

                    <span class="flow-arrow">→</span>

                    <span class="flow-label">To:</span>
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
                        A${String(v.owasp || "N/A").padStart(2, "0")}:2025
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

        const severity = getSeverityClass(
            (a.accuracy_attack / 100) * 10
        )

        return `
        <div class="card attack-card ${severity}">

            <div class="card-header">

                <div>
                    <div class="card-title">
                        ${a.nombre}
                    </div>

                    <div class="card-subtitle">
                        Exactitud: ${a.accuracy_attack}%
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
                        ${a.capec.map(c => `CAPEC-${c.id}`).join(", ")}
                    </p>

                    <p>
                        <strong>Vulnerabilidades correlacionadas:</strong>
                    </p>

                    <ul>
                        ${a.vulnerabilidades_involucradas.map(v => `
                            <li>
                                ${v.vulnerability} (CWE-${v.cwe})
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

        const accuracy = ataque.accuracy_attack || 0

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

        if (data.type === "attack") {

            details.innerHTML = `

                <h4>${data.label}</h4>

                <p><b>Resultado:</b> ${data.resultado}</p>

                <p><b>Exactitud:</b> ${data.accuracy}%</p>

                <p><b>Descripción:</b> ${data.descripcion}</p>
            `
        }

        else {

            details.innerHTML = `

                <h4>${data.label}</h4>

                <p><b>CWE:</b> ${data.cwe}</p>

                <p><b>CVSS:</b> ${data.cvss}</p>

                <p><b>Impacto:</b> ${data.impact}</p>

                <p><b>Probabilidad:</b> ${data.probability}</p>

                <p><b>Archivo:</b> ${data.file}</p>
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