def ats_breakdown(
        skill_score,
        structure_score,
        keyword_score):

    final_score = (
        skill_score * 0.5
        +
        structure_score * 0.3
        +
        keyword_score * 0.2
    )

    return {

        "Skill Match":
            round(skill_score,2),

        "Resume Structure":
            round(structure_score,2),

        "Keyword Density":
            round(keyword_score,2),

        "Final ATS Score":
            round(final_score,2)
    }