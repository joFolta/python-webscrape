# https://towardsdatascience.com/how-to-collect-data-from-any-website-cb8fad9e9ec5

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)

# Could not find a version that satisfies the requirement time (from versions: )
# No matching distribution found for time
import time 

import requests

#   Could not find a version that satisfies the requirement random (from versions: )
# No matching distribution found for random
import random

# ACCESSING THE WEBSITE
page = requests.get('http://quotes.toscrape.com/')
# print(page)
# <Response [200]>

# PARSING THE WEBSITE
soup = bs(page.content)
# print(soup)
# Print website's HTML
# <span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>

# HTML INFORMATION FOR NAVIGATION
# soup.find_all(class_='text')
# print(soup.find_all(class_='text'))
classTextSoup = soup.find_all(class_='text')
# print(classTextSoup)
# <span class="text" itemprop="text">“I have not failed. I've just found 10,000 ways that won't work.”</span>, <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>, ...

quotes = [i.text for i in classTextSoup]
# print(quotes)
# ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", '“Try not to become a man of success. Rather become a man of value.”', '“It is better to be hated for what you are than to be loved for what you are not.”', "“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", '“A day without sunshine is like, you know, night.”']

authors = [i.text for i in soup.find_all(class_='author')]
print(authors)

# ACCESSING MULTIPLE PAGES

# TODO: need to figure out why time and random are not installing