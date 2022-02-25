import csv

def save_to_file(jobs):
    file=open("./Python with BeautifulSoup/jobs.csv",mode="w")
    writer=csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        if job !=None:
            writer.writerow(list(job.values()))
    return