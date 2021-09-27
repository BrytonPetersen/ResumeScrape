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
        get_detail_data(soup)


def get_detail_data(soup): #Scrapes the data of the webpage associated with the search url
    href_link = []
    right_link = []
    for link in soup.find_all('a'):
        print(link.get('href'))
        #part = str(EachPart)

def main():
    print("What kind of job are you looking for?")
    job = 'Computer Science'
    #input('> ')
    print("Where city are you hoping to work in?")
    city = 'Fort Collins'
    #input('> ')
    print("What state is that city in?")
    state = 'CO'
    #input('>')
    #f string to put search into url
    search = (f'https://www.indeed.com/jobs?q={job}&l={city}%2C {state}')
    print(search)
    lookup(search)


#call the main funcion
if __name__ == '__main__':
    main()