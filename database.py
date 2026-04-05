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
                status TEXT DEFAULT 'Applied',
                date_applied TEXT
        )
    """)

    con.commit()
    con.close()


def add_job(job: Job):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        INSERT INTO jobs(finn_code, title, description, company, location, url, status, date_applied)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        job.finn_code,
        job.title,
        job.description,
        job.company,
        job.location,
        job.url,
        job.status,
        job.date_applied
    ))

    con.commit()
    con.close()


def get_all_jobs():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        SELECT *
        FROM jobs
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    con.close()
    return rows

def get_job_by_id(job_id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
    row = cur.fetchone()

    con.close()
    return row

def update_job(job_id, job):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        UPDATE jobs
        SET title=?, description=?, company=?, location=?, url=?, status=?
        WHERE id=?
    """, (
        job.title,
        job.description,
        job.company,
        job.location,
        job.url,
        job.status,
        job_id
    ))

    con.commit()
    con.close()
