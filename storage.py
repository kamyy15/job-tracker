import json
import os

def load_job_applications(): # load from JSON into a list to interact with jobs.
    jobs = []

    if os.path.isfile("jobs.json"):
        print('File exists')
        with open("jobs.json", 'r', encoding='utf-8') as file:
            jobs  = json.load(file)
            return jobs
    
    return jobs

def save_job_applications(jobs):
    with open("jobs.json", 'w') as file:
        json.dump(jobs, file)