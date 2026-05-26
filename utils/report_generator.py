from reportlab.pdfgen import canvas


def create_report(
        ats_score,
        match_score,
        missing_skills):

    file_name = "report.pdf"

    pdf = canvas.Canvas(file_name)

    pdf.drawString(
        100,
        800,
        "Resume Analysis Report"
    )

    pdf.drawString(
        100,
        760,
        f"ATS Score: {ats_score}%"
    )

    pdf.drawString(
        100,
        730,
        f"Match Score: {match_score}%"
    )

    pdf.drawString(
        100,
        700,
        f"Missing Skills: {','.join(missing_skills)}"
    )

    pdf.save()

    return file_name