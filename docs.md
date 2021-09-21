# Project Notes
__Plan:__ To scrape data from either resumes or job postings to look for key words
* Possible additions: 
    - Find a relationship between keywords and salary
    - Find relationship between keywords and specific companies
* Two week schedule:
    Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
    ---|---|---|---|---|---|---| 
    Brainstorm ideas and develop a timeline | Decide which hiring sites to use and look at their HTML | Read beautiful soup documentation | Learn ways to efficiently count word repetition | Write script to scrape data | Write script to scrape data |
    Write script to organize data | Write script to organize data | Write script to visualize the data | Create a report in MD | Clean up bugs - record walkthrough | Clean up bugs |  |
__Potentially Useful Websites__
* https://www.postjobfree.com
* https://www.livecareer.com/resume-search/search?jt=computer%20science

__Notes__:
* Most well-populated websites require payment for employers to browse resumes - it may be easier to browse job listings instead
    - Would be useful because I don't care about what people are submitting, I care about what employers are looking for
* Data scraping: 
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
    - Here is another interesting example using NLP: Bag of Words and Scikit-learn libraries : https://www.analyticsvidhya.com/blog/2021/08/a-friendly-guide-to-nlp-bag-of-words-with-python-example/
        - This example reads the words into a dataset and then counts their frequency - this could be a good solution to making it work well with bs4
    