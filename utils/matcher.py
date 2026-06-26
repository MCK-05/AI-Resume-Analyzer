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