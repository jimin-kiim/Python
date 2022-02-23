import requests
from bs4 import BeautifulSoup
from indeed import extract_pages, extract_jobs

last_page=extract_pages()

jobs=extract_jobs(last_page)
print(jobs)