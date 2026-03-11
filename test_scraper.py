from scraper import extract_finn_code, fetch_job_from_finn

def main():
    text = input("Enter url or code")
    code = extract_finn_code(text)

    if not code:
        print("Invalid finn coed")
        return
    
    job = fetch_job_from_finn(code)

    print("\nJob: ")
    print(job)


if __name__ == "__main__":
    main()