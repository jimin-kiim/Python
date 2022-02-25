import re
import requests
from bs4 import BeautifulSoup

LIMIT=50
URL=f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}&vjk=43a7c98bbd0875ed"

def extract_pages():
    result = requests.get(URL)
    # print(result)
    # print(result.text)
    # bringing all the html codes

    soup= BeautifulSoup(result.text,'html.parser')
    # print(soup)
    pagination= soup.find("div",{"class":"pagination"})
    links=pagination.find_all("a")
    # print(pages)
    pages=[]
    for link in links[:-1] : 
    # get all the items except for the last one.
        pages.append(int(link.string))
        # link.find("span").string results the same. 
    # print(pages)
    max_page=pages[-1]

    return max_page

def extract_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        result= requests.get(f"{URL}&start={page*LIMIT}")
        soup=BeautifulSoup(result.text,'html.parser')
        results=soup.find_all("a",{"class":"fs-unmask"})
        for result in results:
            jobs.append(extract_job(result))
    return jobs

def extract_job(html):
    title=(html.find("h2",{"class":"jobTitle"})).find("span").string
    company=(html.find("span",{"class":"companyName"})).string
    location=(html.find("div",{"class":"companyLocation"})).text
    id=html["data-jk"]
    if title != "new":
        return {'title':title,'company':company,'location':location,'link':f"https://www.indeed.com/viewjob?jk={id}"}

def get_jobs():
    last_page=extract_pages()
    jobs=extract_jobs(last_page)        
    return jobs