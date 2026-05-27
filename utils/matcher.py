skills_database = [

    "python",
    "java",
    "c",
    "c++",

    "sql",
    "mysql",
    "postgresql",

    "html",
    "css",
    "javascript",

    "react",
    "nodejs",

    "spring boot",

    "git",
    "github",

    "aws",
    "docker",

    "etl",
    "data analysis",
    "power bi",

    "spark",
    "pyspark",

    "apache airflow",

    "machine learning",
    "deep learning",
    "nlp",

    "tensorflow",
    "pandas",
    "numpy"
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