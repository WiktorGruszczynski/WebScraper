from webscraper import processor
from webscraper import scrape
from time import time


url = f"https://google.com"
iterations = 100

url_list = [url for i in range(iterations)]


t0=time()
results = processor.iterate(function = scrape, Iterlist=url_list)
t1=time()


print(f"Execution time: {round(t1-t0,2)} seconds")

