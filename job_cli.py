from database import init_db, add_job
from scraper import extract_finn_code, fetch_job_from_finn
from models import Job

def manual_job():
    title = input("Title: ")
    company = input("Company: ")
    #location = input("Location: ")

    return Job(
        finn_code=None,
        title=title,
        company=company,
        description="",
        location="Unknown",
        status="",
        url=None
    )

def main():
    init_db()

    choice = input()