from reportlab.pdfgen import canvas
from reportlab.lib.colors import blue


def create_report(
        ats_score,
        match_score,
        missing_skills,
        resume_skills,
        jd_skills,
        breakdown,
        keyword_density,
        ai_suggestions
):

    file_name = "Resume_Report.pdf"

    pdf = canvas.Canvas(file_name)

    y = 800

    # -------------------------------
    # Title
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(blue)

    pdf.drawString(
        160,
        y,
        "AI Resume Analysis Report"
    )

    y -= 40

    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Helvetica", 12)

    # -------------------------------
    # Scores
    # -------------------------------

    pdf.drawString(
        50,
        y,
        f"ATS Score : {ats_score}%"
    )

    y -= 20

    pdf.drawString(
        50,
        y,
        f"Skill Match Score : {match_score}%"
    )

    y -= 30

    # -------------------------------
    # Resume Skills
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "Resume Skills"
    )

    y -= 20

    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        60,
        y,
        ", ".join(resume_skills)
    )

    y -= 30

    # -------------------------------
    # JD Skills
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "Job Description Skills"
    )

    y -= 20

    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        60,
        y,
        ", ".join(jd_skills)
    )

    y -= 30

    # -------------------------------
    # Missing Skills
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "Missing Skills"
    )

    y -= 20

    pdf.setFont("Helvetica", 11)

    if len(missing_skills) == 0:

        pdf.drawString(
            60,
            y,
            "None"
        )

    else:

        pdf.drawString(
            60,
            y,
            ", ".join(missing_skills)
        )

    y -= 35

    # -------------------------------
    # ATS Breakdown
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "ATS Breakdown"
    )

    y -= 20

    pdf.setFont("Helvetica", 11)

    for key, value in breakdown.items():

        pdf.drawString(
            60,
            y,
            f"{key} : {value}"
        )

        y -= 18

    y -= 10

    # -------------------------------
    # Keyword Density
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "Keyword Density"
    )

    y -= 20

    pdf.setFont("Helvetica", 11)

    for key, value in keyword_density.items():

        pdf.drawString(
            60,
            y,
            f"{key} : {value}"
        )

        y -= 18

    y -= 10

    # -------------------------------
    # AI Suggestions
    # -------------------------------

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        50,
        y,
        "AI Suggestions"
    )

    y -= 20

    pdf.setFont("Helvetica", 10)

    lines = ai_suggestions.split("\n")

    for line in lines:

        if y < 50:

            pdf.showPage()

            pdf.setFont("Helvetica", 10)

            y = 800

        pdf.drawString(
            60,
            y,
            line[:110]
        )

        y -= 15

    pdf.save()

    return file_name