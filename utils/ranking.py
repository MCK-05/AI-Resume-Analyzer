from utils.parser import extract_text

from utils.ats import calculate_ats_score


def rank_resumes(
        resumes,
        jd):

    results = []

    for resume in resumes:

        text = extract_text(
            resume
        )

        score = calculate_ats_score(
            text,
            jd
        )

        results.append({

            "Resume":
                resume.name,

            "ATS Score":
                score
        })

    results.sort(

        key=lambda x:
        x["ATS Score"],

        reverse=True
    )

    return results