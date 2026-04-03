import requests
from bs4 import BeautifulSoup
import re
from models import Job
from datetime import datetime

def extract_finn_code(text):
    match = re.search(r"(\d{8,})", text)
    return match.group(1)

def fetch_job_from_finn(finn_code: str) -> Job:
    url = f"https://www.finn.no/job/ad/{finn_code}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    title_tag = soup.find("h2", class_="t2 md:t1 mb-6")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown"

    company_tag = soup.find("p", class_="mb-24")
    company = company_tag.get_text(strip=True) if company_tag else "Unknown"


    location = "Unknown"

    date_applied = datetime.now().strftime("%d-%m-%Y")


    return Job(
        finn_code=finn_code,
        title=title,
        description="",
        company=company,
        location=location,
        url="",
        status="Test",
        date_applied=date_applied
    )
