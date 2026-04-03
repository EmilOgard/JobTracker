from database import init_db, add_job, get_all_jobs
from scraper import extract_finn_code, fetch_job_from_finn

def edit_job(job):
    print("Edit job")

    title = input(f"Title [{job.title}]: ")
    if title:
        job.title = title
    

    company = input(f"Company [{job.company}]: ")
    if company:
        job.company = company
    

    location = input(f"Location [{job.location}]: ")
    if location:
        job.location = location
    

    description = input(f"Description [{job.description}]: ")
    if description:
        job.description = description
    

    status = input(f"Status [{job.status}]: ")
    if status:
        job.status = status

    return job


def main():
    init_db()

    text = input("Enter url or code: ")
    code = extract_finn_code(text)

    if not code:
        print("Invalid finn coed")
        return
    
    job = fetch_job_from_finn(code)

    while True:
        print("\nJob: ")
        print(job)

        text = input("\n(a)dd, (e)edit or (d)iscard?").lower()

        if text == "a":
            add_job(job)
            print("Added job to db")
            break
        elif text == "e":
            print("todo, edit")
            job = edit_job(job)
        elif text == "d":
            print("todo, discard")
            break
        else:
            print("unknown command")


if __name__ == "__main__":
    main()