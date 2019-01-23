import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page=1
    while page<=max_pages:
        url= 'https://en.wikipedia.org/wiki/Web_scraping'
        source_code = requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a', {"class" : "firstHeading"}):
            href = link.get('href')
            title=link.string
            print(href)
            print(title)
trade_spider(1)