import sqlite3
from models import Job

DB_NAME = "jobs.db"

def init_db():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                finn_code TEXT,
                title TEXT,
                description TEXT,
                company TEXT,
                location TEXT,
                url TEXT,
                status TEXT DEFAULT 'Applied'
        )
    """)

    con.commit()
    con.close()


def add_job(job: Job):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        INSERT INTO jobs(finn_code, title, description, company, location, url, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        job.finn_code,
        job.title,
        job.description,
        job.company,
        job.location,
        job.url,
        job.status
    ))

    con.commit()
    con.close()


def get_all_jobs():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        SELECT id, finn_code, title, company, location, description, status
        FROM jobs
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    con.close()
    return rows