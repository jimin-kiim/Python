from json import load
import re
import requests
from bs4 import BeautifulSoup

URL=f"https://stackoverflow.com/jobs?q=python&sort=i"

def extract_pages():
    result=requests.get(URL)
    soup=BeautifulSoup(result.text,'html.parser')
    paginations= (soup.find("div",{"class":"s-pagination"})).find_all("span")
    last_page=int(paginations[-2].string)
    return last_page

def extract_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        result= requests.get(f"{URL}&pg={page+1}")
        soup=BeautifulSoup(result.text,'html.parser')
        results=soup.find_all("div",{"class":"-job"})
        for result in results:
            jobs.append(extract_job(result))
    return jobs

def extract_job(html):
    title=(html.find("a",{"class":"s-link"})).string
    company_row=html.find("h3").find_all("span")
    company=(company_row[0].string)
    location=(company_row[1].string).strip()
    
    # id=html["data-jk"]
    if title != "new":
        return {'title':title,
        'company':company,
        'location':location,
        # 'link':f"https://www.indeed.com/viewjob?jk={id}"
        }

def get_jobs():
    last_page=extract_pages()
    jobs=extract_jobs(last_page)        
    return jobs


print(get_jobs())