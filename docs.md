# Project Notes
__Plan:__ To scrape data from either resumes or job postings to look for key words. This will be useful in determining what to study and what to include on a resume.
* Possible additions: 
    - Find a relationship between keywords and salary
    - Find relationship between keywords and specific companies
* Two week schedule (goals to keep me motivated - I should make them more specific before I start):
    Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
    ---|---|---|---|---|---|---| 
    Brainstorm ideas and develop a timeline | Decide which hiring sites to use and look at their HTML | Read beautiful soup documentation | Learn ways to efficiently count word repetition | Write script to scrape data | Write script to scrape data |
    Write script to organize data | Write script to organize data | Write script to visualize the data | Create a report in MD | Clean up bugs - record walkthrough | Clean up bugs |  |
__Potentially Useful Websites for Data:__
* https://www.postjobfree.com
* https://www.livecareer.com/resume-search/search?jt=computer%20science

__Potentially Useful Websites for Documentation:__
* https://beautiful-soup-4.readthedocs.io/en/latest/

__Notes__:
* Most well-populated websites require payment for employers to browse resumes - it may be easier to browse job listings instead
    - Would be useful because I don't care about what people are submitting, I care about what employers are looking for
* Data scraping: 
    - This is an example of data scraping taken from an old project I did:
    ``` python
    import matplotlib.pyplot as plt
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re
    import tkinter as tk


    #use the requests module to get the bytes from the ebay page from the user search
    def get_page(url,search):
        response = requests.get(url)
        #make sure the server responded appropriately. If it didn't, print the response code. If it did, parse the html using the BeautifulSoup module
        if not response.ok:
            print('Server responded: ', response.status_code)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            get_detail_data(soup,search)



    #find the appropriate HTML tags and class names using BeautifulSoup. Store the item names and the costs in two separate lists
    def get_detail_data(soup,search):
        cost = []
        item = []
        products = soup.find_all('h3', class_='s-item__title')
        prices = soup.find_all('span', class_="s-item__price")

    # remove any additional HTML until you are left with only text using .text.strip()
        for price in prices:
            cost.append(price.text.strip())
        for product in products:
            item.append(product.text.strip())
        fix_lists(search,item,cost)



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
        
        

    #get the user's desired ebay search
    def main():
        base_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='
        search = input("Please enter your search: ")
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
    ```
    - Here are some important HTML tags from indeed.com
        - nice
* Word frequency: 
    - Here is a really useful example but it reads out of a text file so it may be difficult to implement while using bs4 library (taken with permission from https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0 annotated with """text"""):
    ```python
    import collections
    import pandas as pd
    import matplotlib.pyplot as plt
    %matplotlib inline# Read input file, note the encoding is specified here 
    # It may be different in your text file
    """
    His code uses .txt files. I may need to read
    """
    file = open('PrideandPrejudice.txt', encoding="utf8")
    a= file.read()# Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['mr','mrs','one','two','said']))# Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1# Print most common word
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)# Close the file
    file.close()# Create a data frame of the most common words 
    # Draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')
    ```
    - Here is another interesting example using NLP-Bag of Words and Scikit-learn libraries: https://www.analyticsvidhya.com/blog/2021/08/a-friendly-guide-to-nlp-bag-of-words-with-python-example/
        - This example reads the words into a dataset and then counts their frequency - this could be a good solution to making it work well with bs4
        - It would also make it easier to find relationships between keywords and company/ salary
    - Or consider this one for similar reasons: https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/
    