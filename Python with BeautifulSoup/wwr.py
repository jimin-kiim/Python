import requests
from bs4 import BeautifulSoup

def extract_jobs(url):
    jobs=[]
    result= requests.get(url)
    soup=BeautifulSoup(result.text,'html.parser')
    results=soup.find_all("li",{"class":"feature"})
    for result in results:
        jobs.append(extract_job(result))
    return jobs

def extract_job(html):
    title=(html.find("span",{"class":"title"})).string
    company_values=html.find_all("span",{"class":"company"})
    company=company_values[0].get_text(strip=True)
    location=company_values[2].get_text(strip=True)
    anchor=html.find_all("a")
    link=anchor[1]["href"]
    return {'title':title,'company':company,'location':location,'link':f'https://weworkremotely.com{link}'}

def get_wwr_jobs(word):
    url=f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs=extract_jobs(url)  

    return jobs