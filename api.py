from fastapi import FastAPI
from storage import get_all_jobs, add_job_db
from jobs import view_jobs
from pydantic import BaseModel
from typing import Optional

app = FastAPI() # creates FastAPI app

class Job(BaseModel):
    date_posted: str
    company_name: str
    position: str
    status: str
    location: str
    work_environment: str
    employment_type: str
    pay: float
    date_applied: str
    deadline: Optional[str] = None
    contact: Optional[str] = None
    URL: str
    resume_version: str
    notes: Optional[str] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/jobs")
def get_jobs():
    jobs = get_all_jobs()
    return [dict(application) for application in jobs] # list comprehension - concise way to loop through a list and transform each item.

@app.post("/jobs")
def add_job_application(job: Job): # tells FastAPI to look for a request in the format of Job and then pass the arguments in job to addjobdb's parameters by calling them as objects in job
    add_job_db(job.date_posted, job.company_name, job.position, job.location, job.work_environment, job.employment_type, job.pay, job.date_applied, job.deadline, job.status, job.contact, job.URL, job.resume_version, job.notes)
    return {"message": "Job added successfully."} # Python dictionary convention that FastAPI converts to JSON and returns a message so the frontend knows what happend.