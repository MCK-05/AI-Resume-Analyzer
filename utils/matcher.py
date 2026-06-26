import pandas as pd

skills_database = pd.read_csv(
    "data/skills.csv"
)["skill"].tolist()


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text:

            found_skills.append(skill)

    return list(set(found_skills))
def calculate_match(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0

    matched = set(resume_skills) & set(jd_skills)

    score = (len(matched) / len(jd_skills)) * 100

    return round(score, 2)