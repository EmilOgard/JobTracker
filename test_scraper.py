from database import init_db, add_job
from scraper import extract_finn_code, fetch_job_from_finn

def main():
    init_db()

    text = input("Enter url or code")
    code = extract_finn_code(text)

    if not code:
        print("Invalid finn coed")
        return
    
    job = fetch_job_from_finn(code)

    print("\nJob: ")
    print(job)

    add_job(job)
    print("Added job to db");


if __name__ == "__main__":
    main()