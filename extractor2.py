from bs4 import BeautifulSoup
import requests
import re

url = "https://www.google.com"
html_doc = requests.get(url).text


soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
