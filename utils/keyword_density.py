from collections import Counter


def keyword_density(
        resume_text,
        jd_skills):

    resume_text = resume_text.lower()

    counts = {}

    for skill in jd_skills:

        counts[skill] = resume_text.count(
            skill.lower()
        )

    return counts