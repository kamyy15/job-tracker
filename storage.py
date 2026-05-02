import sqlite3

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
    
def add_job_db(date_posted, company_name, position, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes): #don't need jobs or id parameters - id parameter is being handles by AUTOINCREMENT.
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO jobs ( date_posted, company_name, position, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ( date_posted, company_name, position, location, work_environment, employment_type, pay, date_applied, deadline, status, contact, URL, resume_version, notes)) # sqlite takes what's passed into the tuple and puts them in place of the value placeholders.
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

