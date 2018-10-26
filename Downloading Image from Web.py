# Web image Downloader
import random
#module required for fetching image
import urllib.request

def download_image(url):
    name=random.randrange(1,5)
    fullname=str(name)+'.jpg'
    urllib.request.urlretrieve(url,fullname)
# pass th url in funct as a string not as th parameter
download_image("https://web.njit.edu/~sg952/images/avatar1.jpg")
