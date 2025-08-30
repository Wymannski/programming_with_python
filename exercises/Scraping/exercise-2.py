import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(response.content,'html.parser')

    print(soup.find_all('a'))

    for a_tag in soup.find_all('a'):
        href = a_tag['href']
        if "mailto:" in href:
            print(href.split(':')[1])



if __name__ == '__main__':
    main()