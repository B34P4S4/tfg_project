from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from xml.sax.saxutils import escape

from datetime import datetime
from pathlib import Path


def generar_reporte_pdf(data):

    base_dir = Path(__file__).resolve().parent  
    filename = f"vucan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    full_path = base_dir / filename

    doc = SimpleDocTemplate(
        str(full_path),
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    # =====================================================
    # TITULO
    # =====================================================

    elements.append(
        Paragraph(
            "Resultado del análisis de vulnerabilidades generado por VucanAI 2.0",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # RESUMEN
    # =====================================================

    vulns = data.get("vulnerabilidades", [])
    ataques = data.get("ataques", {}).get("ataques_detectados", [])

    resumen = f"""
    <b>Total vulnerabilidades:</b> {len(vulns)}<br/>
    <b>Total ataques correlacionados:</b> {len(ataques)}
    """

    elements.append(
        Paragraph(
            resumen,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 25))

    # =====================================================
    # VULNERABILIDADES
    # =====================================================

    elements.append(
        Paragraph(
            "Vulnerabilidades Detectadas",
            styles["Heading1"]
        )
    )

    for v in vulns:

        descripcion = escape(v.get("description","N/A"))

        text = f"""
        <b>{v.get("vulnerability","N/A")}</b><br/><br/>
        <b>CWE:</b> {v.get("cwe","N/A")}<br/>
        <b>CVSS:</b> {v.get("cvss","N/A")}<br/>
        <b>Impacto:</b> {v.get("impact","N/A")}/5<br/>
        <b>Probabilidad:</b> {v.get("probability","N/A")}/5<br/>
        <b>Ruta:</b> {v.get("file","N/A")}<br/>
        <b>Desde la línea:</b> {v.get("source","N/A")}<b> hasta la línea:</b> {v.get("sink","N/A")}<br/>
        <b>OWASP:</b> A{str(v.get("owasp", "N/A")).zfill(2)}:2025<br/>
        <b>CAPEC:</b> {v.get("capec","N/A")}<br/>
        <b>Descripción:</b><br/>
        {descripcion}
        """

        elements.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 20))

    elements.append(PageBreak())

    # =====================================================
    # ATAQUES
    # =====================================================

    elements.append(
        Paragraph(
            "Ataques Correlacionados",
            styles["Heading1"]
        )
    )

    for a in ataques:

        vulns_html = ""

        for v in a.get("vulnerabilidades_involucradas", []):

            vulns_html += f"""
            - {v.get("vulnerability")} (CWE-{v.get("cwe")})<br/>
            """

        capecs = ", ".join([
            f"CAPEC-{c['id']}"
            for c in a.get("capec", [])
        ])

        accuracy = round((a.get("accuracy_attack") or 0) * 100, 2)

        text = f"""
        <b>{a.get("nombre","N/A")}</b><br/><br/>

        <b>Resultado:</b> {a.get("ataque_resultante","N/A")}<br/>
        <b>Exactitud:</b> {accuracy}%<br/>
        <b>Descripción:</b><br/>
        {a.get("descripcion","N/A")}<br/><br/>

        <b>CAPECs:</b> {capecs}<br/><br/>

        <b>Vulnerabilidades correlacionadas:</b><br/>
        {vulns_html}
        """

        elements.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 25))

    doc.build(elements)

    return str(full_path)