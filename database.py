import sqlite3

# strucure of how the data is handled - doesn't store anything.

def init_jobs_table():
    # connect to the database
    connection = sqlite3.connect("jobs.db") # like open for files; creates a jobs.db file if it doesn't exist, or connects to it if it does.
    # create a cursor
    cursor = connection.cursor()
    # execute the SQL
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_posted TEXT,
            company_name TEXT,
            position TEXT,
            qualifications TEXT,
            job_description TEXT,
            location TEXT,
            work_environment TEXT,
            employment_type TEXT,
            pay REAL,
            date_applied TEXT,
            deadline TEXT,
            status TEXT,
            contact TEXT,
            URL TEXT,
            resume_version TEXT,
            notes TEXT
    )""") #runs sql statement
    # commit
    connection.commit() # saves changes
    #close
    connection.close() # closes connection when done

def init_resumes_table():
    # connect to the database
    connection = sqlite3.connect("jobs.db")
    # create a cursor
    cursor = connection.cursor()
    # execute the SQL
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            summary TEXT,
            education TEXT,
            technical_skills_languages TEXT,
            technical_skills_frameworks_libraries TEXT,
            technical_skills_databases TEXT,
            technical_skills_tools_platforms TEXT,
            project_one TEXT,
            project_two TEXT,
            project_three TEXT,
            experience TEXT,
            updated_at TEXT
        )""")
    connection.commit()
    connection.close()

def init_cover_letters_table():
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS cover_letters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER,
            content TEXT,
            created_at TEXT,
            FOREIGN KEY (application_id) REFERENCES jobs(id)
        )""")
    connection.commit()
    connection.close()


def init_db():
    init_jobs_table()
    init_resumes_table()
    init_cover_letters_table()


