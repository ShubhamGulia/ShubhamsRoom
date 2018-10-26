import requests
from bs4 import BeautifulSoup

def spider():
        url='https://web.njit.edu/~sg952/'
        source_code = requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('a' , {"class" : "label"}):
            href=link.get('href')
            title=link.string
            print(href)
            print(title)
spider()