from storage import load_job_applications
from jobs import add_job, view_jobs, update_status, delete_jobs, filter_status, update_application

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
    print(" 3. Filter by status")
    print(" 4. Update the status of an existing application")
    print(" 5. Update other features of an existing application")
    print(" 6. Delete an application")
    print(" 7. Exit")
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
        status = input("What is the status of your application currently (interested/applied/interviewing/declined)? ")
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
        status = input("Choose a status to filter your applications (interested/applied/interviewing/declined): ")
        print("")
        filter_status(jobs, status)
        print("=================================")
    elif choice == "4":
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
    elif choice == "5":
        update_view = input("Would you like to view your existing applications first? y/n: ")
        if update_view == "y":
            view_jobs(jobs)
        update_id = int(input("Choose an application number to update: "))
        for applications in jobs:
            if applications["id"] == update_id:
                print("Is this the application you want to update?")
                print("")
                view_jobs([applications])
                update_q = input("Choice: ")
                print("")
                if update_q == "y":
                    print("")
                    print("Choose a field to update: ")
                    print("")
                    print("1. Date Posted")
                    print("2. Position")
                    print("3. Location")
                    print("4. Work Environment")
                    print("5. Employment Type")
                    print("6. Pay")
                    print("7. Date Applied")
                    print("8. Deadline To Apply")
                    print("9. Contact")
                    print("10. Resume Version")
                    print("11. Notes")
                    print("")
                    field = int(input("Enter Choice: "))
                    print("")

                    if field == 1:
                        print(f"You've chosen to update the date posted for application number {update_id}.")
                        field = "date_posted"
                    elif field == 2:
                        print(f"You've chosen to update the position for application number {update_id}.")
                        field = "position"
                    elif field == 3:
                        print(f"You've chosen to update the location for application number {update_id}.")
                        field = "location"
                    elif field == 4:
                        print(f"You've chosen to update the work environment for application number {update_id}.")
                        field = "work_environment"
                    elif field == 5:
                        print(f"You've chosen to update the employment type for application number {update_id}.")
                        field = "employment_type"
                    elif field == 6:
                        print(f"You've chosen to update the pay for application number {update_id}.")
                        field = "pay"
                    elif field == 7:
                        print(f"You've chosen to update the date applied for application number {update_id}.")
                        field = "date_applied"
                    elif field == 8:
                        print(f"You've chosen to update the application deadline for application number {update_id}.")
                        field = "deadline"
                    elif field == 9:
                        print(f"You've chosen to update the contact information for application number {update_id}.")
                        field = "contact"
                    elif field == 10:
                        print(f"You've chosen to update the resume version for application number {update_id}.")
                        field = "resume_version"
                    elif field == 11:
                        print(f"You've chosen to update the notes for application number {update_id}.")
                        field = "notes"
                    else:
                        print("Please choose a number from 1-11.")
                    
                    print("")
                    new_value = input("Please enter the update: ")
                    print("")
                
                    update_application(jobs, update_id, field, new_value)

                    
                

    elif choice == "6":
        if jobs:
            view = input("Would you like to view your applications first? y/n:")
            if view == "y":
                view_jobs(jobs)
            remove_id = int(input("Which job application would you like to remove? "))
            delete_jobs(jobs, remove_id)
        else:
            print("Add an application first to get started.")

    elif choice == "7":
        print("See ya soon!")
        break
    else:
        print("Choose an option between 1-4!")

