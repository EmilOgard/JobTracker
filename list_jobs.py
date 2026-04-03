from database import init_db, get_all_jobs


def main():
    init_db()
    jobs = get_all_jobs()

    if not jobs:
        print("No jobs found")
        return

    print("\n List of jobs")
    for job in jobs:
        print(f"""
            Finncode: {job[0]}
            Title: {job[1]}
            Company: {job[2]}
            Location: {job[3]}
            Description: {job[4]}
            Status: {job[5]}
            Date applied: {job[6]}
        """)

if __name__ == "__main__":
    main()