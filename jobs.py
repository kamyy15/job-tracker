from storage import get_all_jobs, add_job_db, update_job_db, delete_job_db, get_jobs_by_status, add_resume_information_db

def add_job(date_posted, company_name, position, qualifications, job_description, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes):
    add_job_db(date_posted, company_name, position, qualifications, job_description, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes)

def view_jobs(jobs): # needs jobs passed in a paramter to see it exists and be able to interact with it.
    if jobs:
        for applications in jobs: # applications is each row
            print(f"{applications['id']}. {applications['company_name']} - {applications['position']}")
            print(f"Date posted: {applications['date_posted']}")
            print(f"Status: {applications['status']}")
            print(f"Location: {applications['location']}")
            print(f"Work Environment: {applications['work_environment']}")
            print(f"Employment Type: {applications['employment_type']}")
            print(f"Pay: {applications['pay']}")
            print(f"Date Applied: {applications['date_applied']}")
            print(f"Deadline: {applications['deadline']}")
            print(f"Contact: {applications['contact']} - URL: {applications['URL']}")
            print(f"Resume Version: {applications['resume_version']}")
            print(f"Notes: {applications['notes']}")
            print("")

    else:
        print('You have no current job apps! Add some first to view them.')

def add_resume_information(full_name, summary, education, technical_skills_1, technical_skills_2, technical_skills_3, technical_skills_4, project_one, project_two, project_three, experience):
    add_resume_information_db(full_name, summary, education, technical_skills_1, technical_skills_2, technical_skills_3, technical_skills_4, project_one, project_two, project_three, experience)

def update_status(update_id, field, new_value):
    update_job_db(update_id, field, new_value)

def delete_jobs(remove_id):
    delete_job_db(remove_id)

def filter_status(status):
    jobs = get_jobs_by_status(status)
    view_jobs(jobs)

def update_application(update_id, field, new_value):
    update_job_db(update_id, field, new_value)


            
            
