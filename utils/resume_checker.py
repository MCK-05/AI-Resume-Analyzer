def check_resume_sections(text):

    text = text.lower()

    sections = {
        "Summary": "summary" in text,
        "Skills": "skills" in text,
        "Projects": "project" in text,
        "Education": "education" in text,
        "Certifications": "certification" in text,
        "Achievements": "achievement" in text
    }

    return sections