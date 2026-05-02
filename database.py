import sqlite3

# strucure of how the data is handled - doesn't store anything.

def init_db():
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
        location TEXT,
        work_environment TEXT,
        employment_type TEXT,
        pay REAL,
        date_applied TEXT,
        deadline TEXT,
        status TEXT,
        contact TEXT,
        URL text,
        resume_version TEXT,
        notes TEXT
    )""") #runs sql statement
    # commit
    connection.commit() # saves changes
    #close
    connection.close() # closes connection when done


