import streamlit as st
import matplotlib.pyplot as plt
from utils.parser import extract_text
from utils.matcher import extract_skills
from utils.matcher import calculate_match
from utils.ai_helper import get_suggestions
from utils.ats import calculate_ats_score
from utils.resume_checker import check_resume_sections
from utils.report_generator import create_report

st.title("AI Resume Analyzer")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_resume and job_description:

    resume_text = extract_text(uploaded_resume)

    ats_score = calculate_ats_score(
    resume_text,
    job_description
    )

    st.subheader("ATS Score")

    st.metric(
    "ATS Score",
    f"{ats_score}%"
    )
    st.progress(int(ats_score))
    
    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    score = calculate_match(
        resume_skills,
        jd_skills
    )

    st.subheader("Resume Skills")
    st.write(resume_skills)

    st.subheader("JD Skills")
    st.write(jd_skills)

    st.subheader("Match Score")
    st.metric(
    "Skill Match Score",
    f"{score}%"
    )

    missing = list(
        set(jd_skills)-set(resume_skills)
    )

    st.subheader("Missing Skills")
    st.write(missing)

    suggestions = get_suggestions(
        resume_text,
        job_description
    )
    
    matched = len(
    set(resume_skills) &
    set(jd_skills)
    )

    missing = len(
    set(jd_skills) -
    set(resume_skills)
    )

    fig, ax = plt.subplots()

    ax.bar(
    ["Matched", "Missing"],
    [matched, missing]
    )

    st.subheader("Skill Match Dashboard")

    st.pyplot(fig)

    sections = check_resume_sections(
    resume_text
    )

    st.subheader(
    "Resume Completeness"
    )

    for section, present in sections.items():

        if present:
            st.success(f"{section} ✓")
        else:
            st.error(f"{section} ✗")

    st.subheader("AI Suggestions")
    st.write(suggestions)

    report_path = create_report(
    ats_score,
    score,
    missing
    )

    with open(
            report_path,
            "rb"
    ) as file:

        st.download_button(
            "Download Report",
            file,
            "Resume_Report.pdf"
        )

try:
    suggestions = get_suggestions(
        resume_text,
        job_description
    )

    st.subheader("AI Suggestions")
    st.write(suggestions)

except Exception as e:
    st.error(f"Gemini Error: {str(e)}")