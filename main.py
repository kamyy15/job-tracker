from storage import load_job_applications
from jobs import add_job, view_jobs, update_status

jobs = load_job_applications()
print("=================================")
print("Welcome to Job Application Tracker!")
print("=================================")
print("")

while True:
    
    print("What would you like to do today?")
    print("")
    print("=================================")
    print(" 1. Add an application")
    print(" 2. View my applications")
    print(" 3. Update the status of an application.")
    print(" 4. Exit")
    print("=================================")
    print("")
    

    choice = input("Enter your choice: ")

    print("")

    if choice == "1":
        print("That's exciting! Enter in information about application below:")
        print("")
        date_posted = input("When was the position posted? ")
        company_name = input("Company Name? ")
        position = input("What is the job position? ")
        location = input ("Where is the job located? ")
        work_environment = input("Remote, Onsite, or Hybrid? ")
        employment_type = input("Part or Full Time? ")
        pay = float(input("What is the pay? "))
        date_applied  = input("What is the date you applied? ")
        deadline = input("Is there an application deadline? ")
        status = input("What is the status of your application currently? ")
        contact = input("Is there a contact? ")
        URL = input("What is the URL? ")
        resume_version = input("What is the resume version you used with this application? ")
        notes = input("Any extra notes? ")
        print("")

        add_job(jobs, date_posted, company_name, position, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes)

        print("Your job has been added :)")
        print("=================================")

    elif choice == "2":
        if jobs:
            print("Current job applications: ")
            print("")
            view_jobs(jobs)
            print("=================================")
        else:
            print("You have no current job applications added! Add one first to get started.")
            print("")
    elif choice == "3":
        if jobs:
            print("Choose an application number to update the status:")
            print("")
            id = int(input("Application number: "))
            print("")
            new_status = input("New status update: ")
            print("")
            update_status(jobs, id, new_status)
        else:
            print("You have no current job applications added. Add one first!")
            print("")
    elif choice == "4":
        print("See ya soon!")
        break
    else:
        print("Choose an option between 1-4!")

