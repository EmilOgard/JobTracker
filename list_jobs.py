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
            ID: {job[0]}
            Finncode: {job[1]}
            Title: {job[2]}
            Company: {job[3]}
            Location: {job[4]}
            Description: {job[5]}
            Status: {job[6]}
        """)

if __name__ == "__main__":
    main()