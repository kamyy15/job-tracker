import sqlite3

def get_all_jobs():
    connection = sqlite3.connect("jobs.db")
    connection.row_factory = sqlite3.Row # tells SQLite to return rows that behave like dictionaries to still do job["company_name"]
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM jobs
    """)
    jobs = cursor.fetchall() # call it and store it in a variable and return it.
    connection.close()
    return jobs # has to be last as once Python hits return it exits function immediately
    
