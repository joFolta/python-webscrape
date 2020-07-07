# python-webscrape

## Setup

- `pip install beautifulsoup4 pandas requests`
- time and random modules: no need to pip install as time is a default module in the python library; just `import time`, `import random`

# What I learned about Python 3: 
- the power and ease of using python (statistics, graphs, scraping data, etc.)
- `len()` to get length of an array
- variations of the `for` loop
- `.extend()` vs `.append()` https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
```
authors.extend([i.text for i in html.find_all(class_='author')])
```
- use of f-String (similar to Javascript's template literals)
```
urls = [f"http://quotes.toscrape.com/page/{i}" for i in range(1, 11)]
```