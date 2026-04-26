from storage import save_job_applications

def add_job(jobs, date_posted, company_name, position, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes):

    job_application = {
        "id" : len(jobs) + 1,
        "date_posted" : date_posted,
        "company_name" : company_name,
        "position" : position,
        "location" : location,
        "work_environment" : work_environment,
        "employment_type" : employment_type,
        "pay" : pay,
        "date_applied" : date_applied,
        "deadline" : deadline, # user passes in none making it a null data type if none.
        "status" : status,
        "contact" : contact,
        "URL" : URL,
        "resume_version" : resume_version,
        "notes" : notes
    }

    jobs.append(job_application) # appends upstes the list in RAM (fast, temporary)

    save_job_applications(jobs) # this writes it to disk (slower, permanent)

def view_jobs(jobs): # needs jobs passed in a paramter to see it exists and be able to interact with it.
    if jobs:
        for applications in jobs: # applications is each row
            print(f"{applications['id']}. {applications['company_name']} - {applications['position']}")
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

def update_status(jobs, id, new_status):
    for applications in jobs:
        if id == applications["id"]:
            applications["status"] = new_status
            save_job_applications(jobs)
            print("Application status has been updated!")
            break
    else:
        print("An application with that id does not exist.")

def delete_jobs(jobs, remove_id):
    for applications in jobs:
        if remove_id == applications["id"]:
            jobs.remove(applications)
            save_job_applications(jobs)
            print("Job application has been removed.")
            break
    else:
        print("An application with that number does not exist.")
