from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text, jd_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [resume_text, jd_text]
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)