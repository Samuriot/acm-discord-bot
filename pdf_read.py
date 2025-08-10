import pdfplumber
from google import genai 

# TODO: takes a file pdf, converts it to plain text
async def read_file(file_name):
    file_buffer = ""
    with pdfplumber.open(file_name) as pdf, open(f"{file_name}_output.txt", "w", encoding="utf-8") as f:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                f.write(t + '\n')
                file_buffer += t + '\n'
    return file_buffer

# TODO: takes a plain text buffer, and calls AI agent to handle resume feedback
async def interpret_buffer(plain_text_resume):
    client = genai.Client()
    prompt = "You are a well-versed and experienced technical recruiter in the Big Tech Industry. Please provide feedback on this resume regarding the strengths and weaknesses of the candidate, as well as noting what can be improved within their resume on a detailed level in the format: Strengths: - x point - y point - z point Points of Improvement: -x point -y point -z point. "
    prompt += "The resume content goes as follows: "
    prompt += plain_text_resume
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    print(response.text)
    return response.text