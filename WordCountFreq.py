from bs4 import BeautifulSoup
import operator
import requests

def start(url):
    word_list=[]
    source_code= requests.get(url).text
    soup= BeautifulSoup(source_code)
    for post_text in soup.findAll('p',{'text-center':''}):
        content= post_text.string
        words= content.lower().split()
        for each_word in words:
          #  print(each_word)
            word_list.append(each_word)
    clean_word(word_list)

# cleaning words which has symbols
def clean_word(word_list):
    clean_word_list=[]
    for word in word_list:
        symbols= ".,/';[]{}?><:@"
        for m in range(0, len(symbols)):
            word = word.replace(symbols[m],"")
        if len(word) > 0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for words in clean_word_list:
        if words in word_count:
            word_count[words] += 1
        else:
            word_count[words] = 1
    for key, value in sorted(word_count.items(), key =operator.itemgetter(0)):
        print(key,value)

start('https://web.njit.edu/~rr524/about.html')
