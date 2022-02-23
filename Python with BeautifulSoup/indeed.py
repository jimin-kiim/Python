import requests
from bs4 import BeautifulSoup
indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50&vjk=43a7c98bbd0875ed")
# print(indeed_result)
# print(indeed_result.text)
# bringing all the html codes

indeed_soup= BeautifulSoup(indeed_result.text,'html.parser')
# print(indeed_soup)
pagination= indeed_soup.find("div",{"class":"pagination"})
links=pagination.find_all("a")
# print(pages)
pages=[]
for link in links[:-1] : 
# get all the items except for the last one.
    pages.append(int(link.string))
    # link.find("span").string results the same. 
# print(pages)
max_page=pages[-1]

for n in range(max_page):
    print("start=",n*50)