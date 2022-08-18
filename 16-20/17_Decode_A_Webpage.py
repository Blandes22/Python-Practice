#webscraper that gets all title of articles from NY Times home page
#unfortunatley the NY Times has odd naming conventions for their classes
#this makes it difficult to scrape only their article titles

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)


soup = BeautifulSoup(r.content, "html.parser")

for articles in soup.find_all("h3"):
    print(articles.get_text())