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
        get_href(soup)


def get_href(soup): # Parses the HTML looking for 'a' tags. Then looks through 'a' tags to get 'href' tags
    href_links = []
    page_links = []
    for link in soup.find_all('a'):
        href_links.append(str((link.get('href'))))
    for href in href_links:
        if 'pagead' in href:
            page_links.append(href)
    get_links(page_links)
    

def get_links(links): #create a new url to scrape using the href tags/ create a new instance of Beautiful Soup
    for link in links:
        search = 'https://indeed.com' + link
        response = requests.get(search)
        if not response.ok:
            print('Server responded: ', response.status_code)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            get_href(soup)
            with open ('wordcount.txt', 'w') as f:
                f.write((soup.get_text()))


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
    search = (f'https://www.indeed.com/jobs?q={job}&l={city}%2C {state}')
    lookup(search)


#call the main funcion
if __name__ == '__main__':
    main()