import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import tkinter as tk
import re


def lookup(search): #Makes a request to the server. If the connection status is ok - move on
    response = requests.get(search)
    if not response.ok:
        print('Server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f'Parsing HTML from {search}...')
        get_href(soup)


def get_href(soup): # Parses the HTML looking for 'a' tags. Then looks through 'a' tags to get 'href' tags
    href_links = []
    page_links = []
    print('Finding al <a> tags...')
    for link in soup.find_all('a'):
        href_links.append(str((link.get('href'))))
    print('Scraping <href> links...')
    for href in href_links:
        if 'vjs=3' in href:
            page_links.append(href)
    #print(len(page_links))
    get_links(page_links)
    

def get_links(links): #create a new url to scrape using the href tags/ create a new instance of Beautiful Soup
    text = ''
    print('Parsing HTML from scraped <href> links...')
    for link in links:
        search = 'https://indeed.com' + link
        #print(search)
        #print(search) ##this will print the new search url
        response = requests.get(search)
        if not response.ok:
            print('Server responded: ', response.status_code)
        else:
            print('Scraping text out of <href> HTML...')
            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup.find_all('div', class_='jobsearch-jobDescriptionText'): # parse new HTML and store all text in 'text' variable. Pass that variable to splitText to be cleaned up and organized
                text += (' ' + soup.get_text())
    wordCount(text)

def wordCount(text): #splitting all of our text into a list so it can be processed easily
    print('Splitting text...')
    words = text.split()
    word_list = []
    clean_word_list = []
    for word in words:
        if word not in word_list:
            word_list.append(word)
    print('Counting...')
    for i in word_list:
        clean_word_list.append(re.sub(r'[^a-z]', '', word_list[i]))
    print([clean_word_list])
    


def main():
    print("What kind of job are you looking for?")
    job = 'Software Engineer'
    #input('> ')
    print("Where city are you hoping to work in?")
    city = 'Fort Collins'
    #input('> ')
    print("What state is that city in?")
    state = 'CO'
    #input('>')
    #f string to put search into url
    search = (f'https://www.indeed.com/jobs?q={job}&l={city}%2C {state}&limit=50&sort=date')
    lookup(search)


#call the main funcion
if __name__ == '__main__':
    main()