import google.generativeai as genai

genai.configure(api_key="AIzaSyCWyeVBgR48pLoFd-A7Q8e9cVsUIU5KBV0")

model = genai.GenerativeModel("gemini-1.5-flash")

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