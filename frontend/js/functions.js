// JAVASCRIP CON LAS FUNCIONES DEL FRONTEND
const API = "http://127.0.0.1:5000/analiza"
const API_ANALISIS = "http://127.0.0.1:5000/analisis"
const btn = document.getElementById("btnAnalizar")
let cy = null
btn.addEventListener("click", analizar)

const btnExportar = document.getElementById("btnExportar")
let ultimoResultado = null
btnExportar.addEventListener("click", exportarPDF)

// CHARTS ESTADISTICAS
let chartSeveridad = null
let chartLenguajes = null
let chartCWE = null
let chartCAPEC = null


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

    const analisisHistoricos = document.getElementById("analisisHistoricos")
    analisisHistoricos.classList.add("hidden")

    if (!ruta) {

        errorBox.innerText = "Error, falta ruta al proyecto que se quiere analizar"
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

        mostrarInfoAnalisis({
            id: data.id || "Nuevo",
            fecha: formatearFecha(new Date()),
            total_vulnerabilidades:data.vulnerabilidades?.length || 0,
            total_ataques:normalizarAtaques(data.ataques).length || 0
        })

        dashboard.classList.remove("hidden")
        renderVulnerabilidades(data.vulnerabilidades)
        renderAtaques(data.ataques)

        setTimeout(() => {
            renderGrafico(data.ataques)
        }, 50)

        renderEstadisticas(data.estadisticas)

        loading.classList.add("hidden")

        // BOTON EXPORTAR
        ultimoResultado = data
        await cargarHistoricoAnalisis()
        btnExportar.classList.remove("hidden")
        btnExportar.disabled = false  
        analisisHistoricos.classList.remove("hidden")     

    }

    catch (e) {

        console.error("ERROR REAL:", e)
        errorBox.innerText = e.message || "Error conectando con backend"
        errorBox.classList.remove("hidden")
        btnExportar.classList.add("hidden")
        analisisHistoricos.classList.remove("hidden")  
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

    console.log("RENDER VULNERABILIDADES:", vulnerabilidades)

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
        console.log("MEDIDAS DE MITIGACION: "+v.mitigation)
        const mitigations =
            Array.isArray(v.mitigation)
                ? v.mitigation
                : typeof v.mitigation === "string"
                    ? [v.mitigation]
                    : [];

        const mitigation =
            mitigations
                .filter(item =>
                    item !== null &&
                    item !== undefined &&
                    String(item).trim() !== ""
                )
                .map(item => `<li>${item}</li>`)
                .join("") || "<li>N/A</li>";

        return `

        <div class="card vuln-card ${severity}">

            <!-- RESUMEN -->
            <div class="card-header">

                <div class="vuln-title">
                    ${v.vulnerability || "N/A"}
                </div>

                <div class="vuln-meta">
                    <a href="${enlace_cwe}" target="_blank">CWE-${v.cwe || "0"}</a> |
                    CVSS ${v.cvss || "0"}/10 ${cvss_string}
                </div>

                <div class="vuln-file">
                    Archivo: ${v.file || "N/A"}
                </div>

                <div class="vuln-flow">
                    <span class="flow-label">Source:</span>
                    ${v.source || "0"}

                    <span class="flow-arrow">→</span>

                    <span class="flow-label">Sink:</span>
                    ${v.sink || "0"}
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
                        ${v.impact || "0"}/5
                        &nbsp; | &nbsp;
                        <strong>Probabilidad:</strong>
                        ${v.probability || "0"}/5
                    </p>

                    <p>
                        <strong>OWASP:</strong>
                        <a href="${enlace_owasp}" target="_blank">${owasp}</a>
                    </p>

                    <!-- <p>
                        <strong>CAPEC:</strong>
                        ${capecs}
                    </p> -->

                    <div class="mitre-section">

                        <strong>MITRE ATT&CK:</strong>

                        <ul>
                            ${mitre}
                        </ul>

                    </div>

                    <div class="mitigation-section">

                        <strong>MEDIDAS DE MITIGACIÓN:</strong>

                        <ul>
                            ${mitigation}
                        </ul>

                    </div>

                </div>

            </details>

        </div>
        `
    }).join("")
}

function normalizarAtaques(ataquesData) {

    if (!ataquesData) return []

    // caso 1: formato nuevo
    if (Array.isArray(ataquesData?.ataques_detectados)) {
        return ataquesData.ataques_detectados
    }

    // caso 2: array directo limpio
    if (Array.isArray(ataquesData)) {

        // si es [array, numero] nos quedamos con el primero
        if (Array.isArray(ataquesData[0])) {
            return ataquesData[0]
        }

        return ataquesData
    }

    return []
}

function renderAtaques(ataquesData) {

    let ataques = normalizarAtaques(ataquesData)

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
                        Grado de cobertura en la correlación: ${accuracy_attack}%  
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
function renderGrafico(ataquesData) {

    let ataques = normalizarAtaques(ataquesData)
    console.log("NORMALIZADO:", ataques)
    const elements = []

    console.log("renderGrafico "+ataques)
    if (!ataques || ataques.length === 0) {

        const div = document.getElementById("correlationGraph")
        div.innerHTML = `
            <div class="empty">
                No se detectaron correlaciones de ataque
            </div>
        `
        return
    }

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
                <p><b>Grado de cobertura en la correlación:</b> ${data.accuracy}%</p>
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

// CARGAR ULTIMOS ANALISIS
async function cargarHistoricoAnalisis() {

    console.log("Cargando históricos analisis")
    try {

        const response = await fetch(API_ANALISIS)
        console.log(response)
        const data = await response.json()
        console.log("DATOS HISTORICO RECUPERADOS: "+data)
        renderHistorico(data)
        console.log("DATA COMPLETA:", data);
        console.log("ESTADISTICAS:", data.estadisticas);
    }
    catch(e) {

        console.error("ERROR CARGAR HISTORICO ANALISIS "+e)
    }
}

function formatearFecha(fechaISO) {

    const fecha = new Date(fechaISO)

    const dia =
        String(fecha.getDate()).padStart(2, "0")

    const mes =
        String(fecha.getMonth() + 1).padStart(2, "0")

    const anio =
        String(fecha.getFullYear()).slice(-2)

    const hora =
        String(fecha.getHours()).padStart(2, "0")

    const minutos =
        String(fecha.getMinutes()).padStart(2, "0")

    const segundos =
        String(fecha.getSeconds()).padStart(2, "0")

    return `${dia}/${mes}/${anio} - ${hora}:${minutos}:${segundos}`
}

// MOSTRAMOS LOS ULTIMOS ANALISIS
function renderHistorico(lista) {

    const div = document.getElementById("listaAnalisis")

    if (!lista || lista.length === 0) {

        div.innerHTML = "<p>No hay análisis previos</p>"
        return
    }

    div.innerHTML = lista.map(a => `

        <div class="analysis-item" onclick="cerrarHistorico(); cargarAnalisis(${a.id},'${a.fecha}')">
            <div class="analysis-id">
                Análisis: #${a.id}
            </div>
            <div class="analysis-date">
                ${formatearFecha(a.fecha)}
            </div>
            <div class="analysis-stats">
                Total vulnerabilidades detectadas:
                ${a.total_vulnerabilidades}
                <br>
                Total ataques correlacionados:
                ${a.total_ataques}
            </div>
        </div>
    `).join("")
}

//MOSTRAMOS ANALISIS SELECCIONADO
async function cargarAnalisis(id,fecha) {

    console.log("Cargando ANALISIS..."+id)
    const errorBox = document.getElementById("errorBox")
    errorBox.classList.add("hidden")

    const dashboard = document.getElementById("dashboard")

    try {

        const response =
            await fetch(
                `${API_ANALISIS}/${id}`
            )

        const data = await response.json()

        mostrarInfoAnalisis({
            id: id,
            fecha: formatearFecha(fecha),
            total_vulnerabilidades: data.vulnerabilidades.length,
            total_ataques: data.ataques.total_ataques
        })

        console.log("DATA RECIBIDA:", data)
        console.log("ID:", id)
        console.log("FECHA:", data.fecha)
        console.log("TOTAL_VULNERABILIDADES:", data.vulnerabilidades.length)
        console.log("TOTAL_ATAQUES:", data.ataques.total_ataques)
        
        dashboard.classList.remove("hidden")  
        renderVulnerabilidades(data.vulnerabilidades)

        console.log("RAW HISTORICO ATAQUES:", data.ataques)
        console.log("FULL DATA:", data)
        console.log("TIPO:", typeof data.ataques)
        console.log("ES ARRAY:", Array.isArray(data.ataques))

        renderAtaques(data.ataques)

        setTimeout(() => {
            renderGrafico(data.ataques)
        }, 50)

        renderEstadisticas(data.estadisticas)

        ultimoResultado = data
        await cargarHistoricoAnalisis()

        btnExportar.classList.remove(
            "hidden"
        )
    }
    catch(e) {

        console.error("ERROR CARGANDO ANALISIS: "+e)
    }
}

function cerrarHistorico() {

    const historyHeader = document.getElementById("historyHeader")
    const listaAnalisis = document.getElementById("listaAnalisis")

    listaAnalisis.classList.add("hidden")
    historyHeader.classList.remove("open")
}

// mostramos informacion del analisis que se muestra en cada momento
function mostrarInfoAnalisis(info) {

    const div = document.getElementById("analisisInfo")

    div.innerHTML = `
        <strong>Mostrando análisis:</strong> #${info.id ?? "Nuevo"}
        &nbsp; | &nbsp;
        <strong>Fecha:</strong> ${info.fecha}
        &nbsp; | &nbsp;
        <strong>Vulnerabilidades:</strong> ${info.total_vulnerabilidades}
        &nbsp; | &nbsp;
        <strong>Ataques correlacionados:</strong> ${info.total_ataques}
    `

    div.classList.remove("hidden")
}

// MOSTRAR ESTADISTICAS GLOBALES DE TODOS LOS ANALISIS GRAFICAMENTE
function renderEstadisticas(stats){
    console.log("ESTADISTICAS RECIBIDAS:", stats);
    if(!stats) return

    renderResumenStats(stats)
    renderSeveridad(stats)
    renderLenguajes(stats)
    renderCWE(stats)
    renderCAPEC(stats)
    
}

function renderResumenStats(stats){

    document.getElementById(
        "statsSummary"
    ).innerHTML = `

        <div class="stats-kpis">

            <div class="kpi">
                <h3>${stats.total_analisis}</h3>
                <span>Análisis</span>
            </div>

            <div class="kpi">
                <h3>${stats.total_vulnerabilidades}</h3>
                <span>Vulnerabilidades</span>
            </div>

            <div class="kpi">
                <h3>${stats.total_ataques}</h3>
                <span>Ataques</span>
            </div>

            <div class="kpi">
                <h3>${stats.total_correlaciones}</h3>
                <span>Correlaciones</span>
            </div>

        </div>
    `
}

function renderSeveridad(stats){

    const s = stats.severidad

    if (chartSeveridad) {
        chartSeveridad.destroy()
    }

    chartSeveridad = new Chart(
        document.getElementById("chartSeveridad"),
        {
            type:"pie",

            data:{
                labels:[
                    "Nº de vulnerabilidades Críticas",
                    "Nº de vulnerabilidades Altas",
                    "Nº de vulnerabilidades Medias",
                    "Nº de vulnerabilidades Bajas"
                ],

                datasets:[{
                    data:[
                        s.criticas,
                        s.altas,
                        s.medias,
                        s.bajas
                    ],
                    backgroundColor: [
                        "#e74c3c",
                        "#f39c12",
                        "#2ecc71",
                        "#3498db"
                    ]
                }]
            }
        }
    )
}

function renderLenguajes(stats){

    const datos = stats.vulnerabilidades_por_lenguaje

    if (chartLenguajes) {
         chartLenguajes.destroy()
    }

    chartLenguajes = new Chart(
        document.getElementById("chartLenguajes"),
        {
            type:"bar",

            data:{
                labels:Object.keys(datos),

                datasets:[{
                    label:"Nº de vulnerabilidades detectadas por lenguaje",
                    data:Object.values(datos),
                    backgroundColor: "#053f0d"
                }]
            }
        }
    )
}

function renderCWE(stats){

    const top = stats.cwe_mas_frecuentes.slice(0,10)

    if (chartCWE) {
         chartCWE.destroy()
    }

    chartCWE = new Chart(
        document.getElementById("chartCWE"),
        {
            type:"bar",

            data:{
                labels:top.map(x => x.cwe),

                datasets:[{
                    label:"CWEs más frecuentes",
                    data:top.map(x => x.total),
                    backgroundColor: "#105cad"
                }]
            }
        }
    )
}

function renderCAPEC(stats){

    console.log("CAPECS:", stats.capec_mas_frecuentes);
    const top = stats.capec_mas_frecuentes.slice(0,10)

    if (chartCAPEC) {
         chartCAPEC.destroy()
    }

    chartCAPEC = new Chart(
        document.getElementById("chartCAPEC"),
        {
            type:"bar",

            data:{
                labels:top.map(x => x.capec),

                datasets:[{
                    label:"CAPECs más frecuentes",
                    data:top.map(x => x.total),
                    backgroundColor: "#c95b11"
                }]
            }
        }
    )
}


// CARGA ULTIMOS ANALISIS AL CARGAR LA PAGINA
window.addEventListener("load", () => {

    console.log("Cargando históricos...")
    cargarHistoricoAnalisis()

    const historyHeader = document.getElementById("historyHeader")
    const listaAnalisis = document.getElementById("listaAnalisis")

    historyHeader.addEventListener("click", (e) => {
        e.stopPropagation()
        listaAnalisis.classList.toggle("hidden")
        historyHeader.classList.toggle("open")
    })

    document.addEventListener("click", (e) => {

        const panel = document.getElementById("analisisHistoricos")

        if (!panel.contains(e.target)) {

            cerrarHistorico()
        }
    })
})
