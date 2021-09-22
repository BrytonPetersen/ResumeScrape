import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import tkinter as tk



def lookup(url,search): #Makes a request to the server. If the connection status is ok - move on
    response = requests.get(url)
    if not response.ok:
        print('Server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        get_detail_data(soup,search)


def get_detail_data(soup,search): #Scrapes the data of the webpage associated with the search url
    
    cost = []
    item = []
    products = soup.find_all('h3', class_='s-item__title') #Looks for HTML tags and indexes assoiciated with the data we are looking for
    prices = soup.find_all('span', class_="s-item__price") # I am not sure if there is a way to avoid hard-coding this in or not
# remove any additional HTML until you are left with only text using .text.strip()
    for price in prices:
        cost.append(price.text.strip())
    for product in products:
        item.append(product.text.strip())
    fix_lists(search,item,cost)

'''

def fix_lists(search,item,cost):
    #use the re module to create a pattern to look for, in this case ##.##
    pattern = re.compile('\d+.\d+')
    new_price = []
    useful_price = []

    #iterate through the cost list and remove the dollar sign, then check to make sure the remaining list matches the pattern made using the re module, then append the list to 'new_price'
    for i in cost:
        noDollar = i.replace('$', '')
        singleVal = pattern.match(noDollar)
        new_price.append(singleVal.group(0))

    #iterate through 'new_price' and make all of the strings into floats so that they can be graphed using matplotlib
    for i in new_price:
        try:
            useful_price.append(float(i))
        except: 
            print("Invalid price format")
    graph_lists(item,useful_price,search)
    


#use matplotlib to graph the prices found on ebay for the item searched by the user. Print out in the terminal the average calculated price, the min, the max, as well as the data frame. 
def graph_lists(item,useful_price,search):
    
    #create a dataframe from the item names and the prices
    d = {'Item: ':item, 'Cost':useful_price}
    df = pd.DataFrame.from_dict(d, orient='index')
    df = df.transpose()
    print(df)

    #plot the graphs
    x_length = []
    x_ef = []
    #in order to create a comprehensible x axis for a scatter plot, i needed to create a list which held the index of each index in the list for the exact length of the 'item' list
    for i in item:
        index = str(item.index(i))
        new = i.replace(i,index)
        x_length.append(new)
    for i in x_length:
        x_ef.append(float(i))

    plt.grid()
    plt.scatter(x_ef, useful_price)
    plt.xlabel(f'Number of {search} found on Ebay')
    plt.ylabel(f"Price of each {search}")
    plt.show()

    out_average_max_min(search, useful_price)



#print the average, max, and min prices of the item searched.
def out_average_max_min(search,useful_price):
    #calculate the average price for the searched item on ebay
    total = 0
    for i in useful_price:
        total += i
    average = total/len(useful_price)
    print(f'The average price for {search} is: $',round(average,2))

    #print the min
    print(f'The minimum price for {search} is: $',min(useful_price))

    #print the max
    print(f'The maximum price for {search} is: $',max(useful_price))
    
    
'''
#get the user's desired ebay search
def main():
    base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='
    print("What kind of job are you looking for?")
    search = input('> ')
    #replace spaces with something that will be readable as a url
    transformed_search = search.replace(" ","+")
    #replace apostrophes with something that will be readable as a url
    adjust_search = transformed_search.replace("'", "%27")
    #add the user search to the base url
    url = base_url + search
    get_page(url,search)


#call the main funcion
if __name__ == '__main__':
    main()