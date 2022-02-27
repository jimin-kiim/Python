import requests
from bs4 import BeautifulSoup

def extract_jobs(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}
    jobs=[]
    result= requests.get(url,headers = headers)
    soup=BeautifulSoup(result.text,'html.parser')
    results=soup.find_all("tr",{"class":"job"})
    for result in results:
        jobs.append(extract_job(result))
    return jobs

def extract_job(html):
    title=(html.find("h2",{"itemprop":"title"})).string.strip()
    company=(html.find("h3",{"itemprop":"name"})).string.strip()
    location=html.find_all("div",{"class":"location"})
    if len(location)>1:
        location=location[0]
    else :
        location="Remote"
    link=html["data-url"]
    return {'title':title,'company':company,'location':location,'link':f'https://remoteok.io{link}'}

def get_ro_jobs(word):
    url=f"https://remoteok.io/remote-dev+{word}-jobs"
    jobs=extract_jobs(url)  

    return jobs