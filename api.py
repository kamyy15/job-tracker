from fastapi import FastAPI
from storage import get_all_jobs, add_job_db, get_resume, get_jobs_by_id, save_cover_letter, add_resume_information_db
from cover_letter import build_cover_letter_prompt, generate_response
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # creates FastAPI app

class Job(BaseModel): # create type called Job - data expected format
    date_posted: str
    company_name: str
    position: str
    qualifications: str
    job_description: str
    location: str
    work_environment: str
    employment_type: str
    pay: float
    date_applied: Optional[str] = None
    deadline: Optional[str] = None
    status: str
    contact: Optional[str] = None
    URL: str
    resume_version: str
    notes: Optional[str] = None

class Resume(BaseModel): # create job type called Resume
    full_name: str
    summary: Optional[str]
    education: str
    technical_skills_1: Optional[str]
    technical_skills_2: Optional[str]
    technical_skills_3: Optional[str]
    technical_skills_4: Optional[str]
    project_one: Optional[str]
    project_two: Optional[str]
    project_three: Optional[str]
    experience: Optional[str]
    

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/jobs")
def get_jobs():
    jobs = get_all_jobs()
    return [dict(application) for application in jobs] # list comprehension - concise way to loop through a list and transform each item.

@app.post("/jobs")
def add_job_application(job: Job): # tells FastAPI to look for a request in the format of Job and then pass the arguments in job to addjobdb's parameters by calling them as objects in job
    add_job_db(job.date_posted, job.company_name, job.position, job.qualifications, job.job_description, job.location, job.work_environment, job.employment_type, job.pay, job.date_applied, job.deadline, job.status, job.contact, job.URL, job.resume_version, job.notes)
    return {"message": "Job added successfully."} # Python dictionary convention that FastAPI converts to JSON and returns a message so the frontend knows what happened.

@app.post("/resume")
def add_resume_information(resume: Resume):
    add_resume_information_db(resume.full_name, resume.summary, resume.education, resume.technical_skills_1, resume.technical_skills_2, resume.technical_skills_3, resume.technical_skills_4, resume.project_one, resume.project_two, resume.project_three, resume.experience)
    return {"message": "Resume information added successfully."}

@app.get("/resume")
def get_resume_information():
    resume = get_resume()
    return dict(resume) # only returns a single row, so doesn't need the list comprehension

@app.get("/jobs/{job_id}")
def get_job_by_id(job_id: int):
    job = get_jobs_by_id(job_id)
    return job

@app.post("/jobs/{job_id}/cover-letter") # {job_id} becomes a paramter FastAPI automatically passes into the function
def generate_cover_letter(job_id: int):
    job = get_jobs_by_id(job_id) # get the job
    resume = get_resume() # get the resume
    prompt = build_cover_letter_prompt(job, resume) # put job and resume in prompt
    cover_letter_text = generate_response(prompt)
    save_cover_letter(job_id, cover_letter_text)
    return {"cover letter": cover_letter_text}

