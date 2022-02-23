import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_pages 


max_page=extract_indeed_pages()

for n in range(max_page):
    print("start=",n*50)