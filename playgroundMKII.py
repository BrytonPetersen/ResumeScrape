import requests
from bs4 import BeautifulSoup
import pandas as pd
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
    print('Splicing text...')
    wordCount(text)

def wordCount(text): #write all of our text into a file so it can be processed easily
    words = text.split()
    clean_list = []
    lower_list = []
    print('Cleaning up...')
    for word in words:
        x = re.sub("[^a-zA-Z]+", "", word) #Using regex to remove anything that is non-alphabetical
        clean_list.append(x)
    while("" in clean_list) :
        clean_list.remove("")
    for item in clean_list:
        lower_list.append(item.lower())
    #print(lower_list)
    search_list = ['python','django','java','javascript','aws','c','frameworks','html','communication','management','analyst','analysis','sales','robotics','knowledge','experience','innovative','software','hardware','remote','data','algorithm','coding','api','design','oracle','jura','distribution','solving','creativity','leadership']
    word_dict = {i:lower_list.count(i) for i in lower_list}
    ordered_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1]) if k in search_list}
    #print(ordered_dict)
    #df = pd.DataFrame.from_dict(ordered_dict)
    #graph(df)
    print(ordered_dict) # could be passed to visually graph it

def graph(df):
    pass

def main():
    print("What kind of job are you looking for?")
    job = input('> ')
    #input('> ')
    print("Where city are you hoping to work in?")
    city = input('> ')
    #input('> ')
    print("What state is that city in?")
    state = input('> ')
    #input('>')
    #f string to put search into url
    search = (f'https://www.indeed.com/jobs?q={job}&l={city}%2C {state}&limit=50&sort=date')
    lookup(search)


#call the main funcion
if __name__ == '__main__':
    main()