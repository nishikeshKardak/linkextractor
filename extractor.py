import requests
import bs4
import urllib

link = input("Enter the url you want to extract")

res = requests.get(link)
page = res.text

#function for taking next target file
def get_next_target(page):
    start_link = page.find('>href=')
    if start_link == -1:
        return None , 0
    #print(start_link)
    start_quote = page.find('"',start_link)
    #print(start_quote)
    end_quote = page.find('"',start_quote+1)
    #print(end_quote)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


#print all links that extract from page
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print (url)
            page = page[endpos:]
        else:
            break

print_all_links(page)
