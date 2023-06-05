import requests
from bs4 import BeautifulSoup

def scrapper(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser').text.split()

        with open('scraper.txt','a') as nigga:
            for line in soup:
                if line.isalpha() and not line.isupper():
                    nigga.write(f'{line.lower()}\n')
    except:
        pass

def link_grabber(cc):
    html = requests.get(f'https://news.google.com/topstories?hl=en-{cc}&gl={cc}&ceid={cc}%3Aen')
    soup = BeautifulSoup(html.content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    links = tuple(filter(None,links))
    print(links)

    for link in links:
        if 'article' in link:
            with open('url.txt','a') as save:
                save.write(f'https://news.google.com{link}\n')

cc = ['GB','MY','AU','US','NZ','SG']

for country in cc:
    link_grabber(country)

with open('url.txt','r') as saved:
    links = saved.read().split('\n')
    for link in links:
        scrapper(link)