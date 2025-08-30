import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(response.content,'html.parser')

    a_tags = soup.find_all('a')

    for tag in a_tags:
        href = tag['href']
        # if 'mailto:' in href:
        if ':' in href:
            print(href.split(':')[1])

if __name__ == '__main__':
    main()