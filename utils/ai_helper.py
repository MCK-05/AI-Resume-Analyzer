import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_suggestions(resume, jd):

    prompt = f"""
    Resume:
    {resume}

    Job Description:
    {jd}

    Give:
    1. Missing skills
    2. Resume improvements
    3. ATS suggestions
    """

    response = model.generate_content(prompt)

    return response.text