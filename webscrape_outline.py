# https://towardsdatascience.com/how-to-collect-data-from-any-website-cb8fad9e9ec5

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)

import time 

import requests

# possibly a default module as well?????
# possibly a default module as well?????
# possibly a default module as well?????
# Could not find a version that satisfies the requirement random (from versions: )
# No matching distribution found for random
import random

# ACCESSING THE WEBSITE
page = requests.get('http://quotes.toscrape.com/') # print(page) # <Response [200]>

# PARSING THE WEBSITE
entireHTML = bs(page.content) # print(entireHTML) # Print website's entire HTML

# PARSE THE HTML INTO QUOTES AND AUTHORS
classTextFromEntireHTML = entireHTML.find_all(class_='text') # print(classTextFromEntireHTML) # [<span class="text"></span>, <span class="text"></span>, <span class="text"></span>, ...]

quotes = [i.text for i in classTextFromEntireHTML] # print(quotes)
# ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", '“Try not to become a man of success. Rather become a man of value.”', '“It is better to be hated for what you are than to be loved for what you are not.”', "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", '“A day without sunshine is like, you know, night.”']

authors = [i.text for i in entireHTML.find_all(class_='author')] # print(authors) 
# ['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']

# ACCESSING MULTIPLE PAGES
# Eg. http://quotes.toscrape.com/page/2/
# python tip: use of f-String (similar to Javascript's template literals)
urls = [f"http://quotes.toscrape.com/page/{i}" for i in range(1, 11)] # print(urls)
# ['http://quotes.toscrape.com/page/1', 'http://quotes.toscrape.com/page/2', 'http://quotes.toscrape.com/page/3', 'http://quotes.toscrape.com/page/4', 'http://quotes.toscrape.com/page/5', 'http://quotes.toscrape.com/page/6', 'http://quotes.toscrape.com/page/7', 'http://quotes.toscrape.com/page/8', 'http://quotes.toscrape.com/page/9', 'http://quotes.toscrape.com/page/10']

# AVOIDING WEB SCRAPING DETECTION
# generate list of values
rate = [i/10 for i in range(10)] # print(rate) # [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# randomly chosing a value from the above list and waiting that amount of time before the loop iterates
time.sleep(random.choice(rate))

# BRINGING IT ALL TOGETHER in the webscrape_execution.py file