import requests
from bs4 import BeautifulSoup

INDEED_URL="https://www.indeed.com/jobs?as_and=python&limit=50&vjk=43a7c98bbd0875ed"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
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