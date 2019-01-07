from bs4 import BeautifulSoup
import requests
import re

url = input("Enter the url ")
html_doc = requests.get(url).text


soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
