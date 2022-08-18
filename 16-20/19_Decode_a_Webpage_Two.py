#2nd webscraper project
#this project takes the article from the url and turns it into one large text block for ease of reading

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

article = soup.select("div.body__inner-container > p")

for i in article:
  print(i.text)