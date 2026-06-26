import streamlit as st
import matplotlib.pyplot as plt

from utils.parser import extract_text
from utils.matcher import extract_skills, calculate_match
from utils.ai_helper import get_suggestions
from utils.ats import calculate_ats_score
from utils.resume_checker import check_resume_sections
from utils.report_generator import create_report
from utils.ats_breakdown import ats_breakdown
from utils.keyword_density import keyword_density
from utils.ranking import rank_resumes


st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.title("AI Resume Analyzer & Job Match Assistant")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_resume and job_description:

    # -------------------------
    # Resume Parsing
    # -------------------------

    resume_text = extract_text(uploaded_resume)

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    # -------------------------
    # Scores
    # -------------------------

    ats_score = calculate_ats_score(
        resume_text,
        job_description
    )

    match_score = calculate_match(
        resume_skills,
        jd_skills
    )

    matched_skills = list(
        set(resume_skills) &
        set(jd_skills)
    )

    missing_skills = list(
        set(jd_skills) -
        set(resume_skills)
    )

    # -------------------------
    # Keyword Density
    # -------------------------

    density = keyword_density(
        resume_text,
        jd_skills
    )

    # -------------------------
    # Resume Structure Score
    # -------------------------

    sections = check_resume_sections(
        resume_text
    )

    structure_score = (
        sum(sections.values()) /
        len(sections)
    ) * 100

    keyword_score = 0

    if len(jd_skills) > 0:

        present_keywords = sum(
            1
            for value in density.values()
            if value > 0
        )

        keyword_score = (
            present_keywords /
            len(jd_skills)
        ) * 100

    breakdown = ats_breakdown(
        ats_score,
        structure_score,
        keyword_score
    )

    # -------------------------
    # Dashboard
    # -------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "ATS Score",
        f"{ats_score}%"
    )

    col2.metric(
        "Skill Match",
        f"{match_score}%"
    )

    col3.metric(
        "Matched Skills",
        len(matched_skills)
    )

    col4.metric(
        "Missing Skills",
        len(missing_skills)
    )

    st.progress(int(ats_score))

    # -------------------------
    # ATS Breakdown
    # -------------------------

    st.subheader("ATS Breakdown")

    st.json(breakdown)

    # -------------------------
    # Skills
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Resume Skills")

        st.write(resume_skills)

    with col2:

        st.subheader("Job Description Skills")

        st.write(jd_skills)

    st.subheader("Missing Skills")

    st.write(missing_skills)

    # -------------------------
    # Chart
    # -------------------------

    fig, ax = plt.subplots()

    ax.bar(
        ["Matched", "Missing"],
        [
            len(matched_skills),
            len(missing_skills)
        ]
    )

    st.subheader("Skill Match Dashboard")

    st.pyplot(fig)

    # -------------------------
    # Resume Completeness
    # -------------------------

    st.subheader("Resume Completeness")

    for section, present in sections.items():

        if present:

            st.success(f"{section} ✓")

        else:

            st.error(f"{section} ✗")

    # -------------------------
    # Keyword Density
    # -------------------------

    st.subheader("Keyword Density")

    st.write(density)

    # -------------------------
    # AI Suggestions
    # -------------------------

    try:

        suggestions = get_suggestions(
            resume_text,
            job_description
        )

        st.subheader("AI Suggestions")

        st.write(suggestions)

    except Exception as e:

        st.error(
            f"Gemini Error: {e}"
        )

    # -------------------------
    # PDF Report
    # -------------------------

    report_path = create_report(
    ats_score,
    match_score,
    missing_skills,
    resume_skills,
    jd_skills,
    breakdown,
    density,
    suggestions
    )

    with open(
        report_path,
        "rb"
    ) as file:

        st.download_button(
            "Download Report",
            file,
            file_name="Resume_Report.pdf",
            mime="application/pdf"
        )

# -----------------------------------------
# Multiple Resume Ranking
# -----------------------------------------

st.markdown("---")

st.header("Multi Resume Ranking")

uploaded_resumes = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_resumes and job_description:

    rankings = rank_resumes(
        uploaded_resumes,
        job_description
    )

    st.table(rankings)