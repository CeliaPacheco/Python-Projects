import requests
from tkinter import *
from bs4 import BeautifulSoup


url = 'https://www.reddit.com/r/dailyprogrammer/'
headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
response = requests.get(url, headers=headers)
html = response.content
soup = BeautifulSoup(html, 'html.parser')


#TODO: Get this working properly, right now it only prints one result
links = {} 
for link in soup.find_all('a'):
    for h2 in link.find_all('h2'):
        if "[Intermediate]" in str(h2):
            links[h2] = link
print(links)
