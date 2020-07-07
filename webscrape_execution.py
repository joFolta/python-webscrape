# https://towardsdatascience.com/how-to-collect-data-from-any-website-cb8fad9e9ec5

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time 
import requests
import random
import openpyxl

authors = []

quotes = []

urls = [f"http://quotes.toscrape.com/page/{i}" for i in range(1, 11)] 

rate = [i/10 for i in range(10)]
rate = [i/10 for i in range(2)]

for url in urls:
  page = requests.get(url)
  html = bs(page.content)
  authors.extend([i.text for i in html.find_all(class_='author')])
  quotes.extend([i.text for i in html.find_all(class_='text')])
  if len(quotes) >= 52: # only need 52 quotes
    break
  time.sleep(random.choice(rate))

# put data into a spread sheet with a Pandas DataFrame
df = pd.DataFrame()
df['Authors'] = authors
df['Quotes'] = quotes

# print out the Pandas DataFrame
print(df)

# create Excel file (.xlsx)
df.to_excel("webscrape.xlsx")