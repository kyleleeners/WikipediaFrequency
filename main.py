import requests
from bs4 import BeautifulSoup
import operator


# retrieve raw word-list
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')
    for post_text in soup.findAll('p'):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

# clean up word-list by removing symbols and empty words
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols =  "1234567890!@#$%^&*()-=_+{}[]|\;':\",./<>?'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
            print(word)
    create_dictionary(clean_word_list)

# create dictionary with words as key and frequency as value, sorted by value
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('replace with wikipedia article')

