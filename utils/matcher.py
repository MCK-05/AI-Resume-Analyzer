skills_database = [
    "python",
    "java",
    "spring boot",
    "mysql",
    "html",
    "css",
    "javascript",
    "aws",
    "docker",
    "git",
    "react",
    "power bi",
    "machine learning"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills

def calculate_match(resume_skills, jd_skills):

    matched = set(resume_skills) & set(jd_skills)

    score = (len(matched) / len(jd_skills)) * 100

    return round(score,2)