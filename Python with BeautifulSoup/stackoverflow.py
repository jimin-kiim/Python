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
    company,location=html.find("h3",{"class":"fc-black-700"}).find_all("span",recursive=False)
    company=company.get_text(strip=True)
    location=location.get_text(strip=True).strip("-")
    id=html["data-jobid"]

    return {'title':title,'company':company,'location':location,'id':id,'link':f'https://stackoverflow.com/jobs/{id}'}
# company.string
# company.get_text(strip=True)

def get_jobs():
    last_page=extract_pages()
    jobs=extract_jobs(last_page)        
    return jobs