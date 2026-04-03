from database import init_db, get_job_by_id, update_job
from models import Job

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

    job_id = input("Enter job ID to edit: ")
    row = get_job_by_id(job_id)

    if not row:
        print("No job found with that ID")
        return
    
    job = Job(
        finn_code=row[1],
        title=row[2],
        description=row[3],
        company=row[4],
        location=row[5],
        url=row[6],
        status=row[7]
    )

    job = edit_job(job)
    update_job(job_id, job)

    print("Job updated")


if __name__ == "__main__":
    main()