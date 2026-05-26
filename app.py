import streamlit as st

from utils.parser import extract_text
from utils.matcher import extract_skills
from utils.matcher import calculate_match
from utils.ai_helper import get_suggestions

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
    st.success(f"{score}%")

    missing = list(
        set(jd_skills)-set(resume_skills)
    )

    st.subheader("Missing Skills")
    st.write(missing)

    suggestions = get_suggestions(
        resume_text,
        job_description
    )

    st.subheader("AI Suggestions")
    st.write(suggestions)