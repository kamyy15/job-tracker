import os
from storage import get_jobs_by_id, get_resume
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def build_cover_letter_prompt(job, resume):
    prompt = f"""
    With the given job application information and resume information, compare the two and 
    write a professional and fitting, yet honest cover letter to the hiring team at the company.
    Keep it one page and avoid generic phrases.

    Job Application Information:
    Company: {job["company_name"]}
    Position: {job["position"]}
    Qualifications: {job["qualifications"]}
    Job Description: {job["job_description"]}

    Resume Information:
    Name: {resume["full_name"]}
    Summary: {resume["summary"]}
    Education: {resume["education"]}
    Technical Languages: {resume["technical_skills_languages"]}
    Frameworks and Libraries: {resume["technical_skills_frameworks_libraries"]}
    Databases: {resume["technical_skills_databases"]}
    Tools: {resume["technical_skills_tools_platforms"]}
    First Project: {resume["project_one"]}
    Second Project: {resume["project_two"]}
    Third Project: {resume["project_three"]}
    Experience: {resume["experience"]}
    """
    return prompt
    
def generate_response(prompt):
    response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
    return response.text