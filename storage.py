import sqlite3
from datetime import datetime

# All CRUD operations (Create, Read, Update, Delete) that interact with tables

def get_all_jobs():
    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row # tells SQLite to return rows that behave like dictionaries to still do job["company_name"]
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM jobs
    """)
    jobs = cursor.fetchall() # reads all and stores them in a Python variable so we can work with them outside of database. Loading it into Python memory.
    connection.close()
    return jobs # has to be last as once Python hits return it exits function immediately
    
def add_job_db(date_posted, company_name, position, qualifications, job_description, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes): #don't need jobs or id parameters - id parameter is being handles by AUTOINCREMENT.
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO jobs ( date_posted, company_name, position, qualifications, job_description, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ( date_posted, company_name, position, qualifications, job_description, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes)) # sqlite takes what's passed into the tuple and puts them in place of the value placeholders.
    connection.commit()
    connection.close()

def update_job_db(update_id, field, new_value):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE jobs SET {field} = ? WHERE id = ?", (new_value, update_id)) # '?' get filled by the tuple (new_value, update_id)
    connection.commit()
    connection.close()

def delete_job_db(remove_id):
    connection  = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM jobs WHERE id = ?
    """, (remove_id,)) # has a comma at the end since its a tuple
    connection.commit()
    connection.close()

def get_jobs_by_status(status):
    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row # tells SQLite to return rows that behave like dictionaries to still do job["company_name"]
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM jobs WHERE status = ?
    """, (status,))
    jobs = cursor.fetchall()
    connection.close()
    return jobs

def get_jobs_by_id(id):
    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM jobs WHERE id = ?
    """, (id,))
    jobs = cursor.fetchone()
    connection.close()
    return jobs

def add_resume_information_db(full_name, summary, education, technical_skills_1, technical_skills_2, technical_skills_3, technical_skills_4, project_one, project_two, project_three, experience):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    updated_at = datetime.now().isoformat()
    cursor.execute("""
    INSERT INTO resumes (full_name, summary, education, technical_skills_languages, technical_skills_frameworks_libraries, technical_skills_databases, technical_skills_tools_platforms, project_one, project_two, project_three, experience, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (full_name, summary, education, technical_skills_1, technical_skills_2, technical_skills_3, technical_skills_4, project_one, project_two, project_three, experience, updated_at))
    connection.commit()
    connection.close()

def get_resume():
    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM resumes
    """)
    resumes = cursor.fetchone()
    connection.close()
    return resumes

def save_cover_letter(job_id, content):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    created_at = datetime.now().isoformat()
    cursor.execute("""
    INSERT INTO cover_letters (application_id, content, created_at) VALUES (?, ?, ?)
    """, (job_id, content, created_at))
    connection.commit()
    connection.close()
    

