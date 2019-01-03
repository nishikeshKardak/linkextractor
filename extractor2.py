import bs4
import requests
import re

web_page = input("Enter the url or link of webpage that you want to extract")

res = requests.get('web_page')
page = res.text


for link in soup.find_all('a'):
    print(link.get('href'))
