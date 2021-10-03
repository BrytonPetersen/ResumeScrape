# Overview

Small scale data scraping project that parses html from fifty job descriptions on indeed.com and shows the most common key words. 

[Software Demo Video](https://youtu.be/4AMYrGFkxKs)

# Purpose

To help me know which skills are most sought after in the job market and where I should focus my studies to best prepare to meet the expectations of employers. 

# Data Analysis Results

Here is an example return from this program for computer science jobs in Denver, CO:

{'creativity': 2, 'html': 3, 'oracle': 5, 'sales': 5, 'solving': 6, 'java': 7, 'coding': 11, 'frameworks': 12, 'innovative': 13, 'python': 14, 'javascript': 15, 'c': 17, 'hardware': 18, 'analysis': 19, 'api': 19, 'remote': 23, 'analyst': 24, 'leadership': 33, 'aws': 41, 'communication': 46, 'design': 56, 'knowledge': 69, 'data': 85, 'management': 88, 'software': 164, 'experience': 227}


# Development Environment

__Environment__
Made in Visual Studio Code on Windows 10 

__Language(s)__
This project was created entirely in python, although I would like to translate it into C++ at some point. 

__Libraries__
- requests library
- bs4 (BeautifulSoup) library
- pandas library
- regular expressions (re) library


# Useful Information and Notes

* [Notes](/docs.md)

# Future Work

* Add a visual for the data
* Find a more efficient way to clean up the data
* Avoid counting html tag id's as text?
* Make it into a larger scale project
* Translate into C++?