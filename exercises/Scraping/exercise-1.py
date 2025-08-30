import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(response.content,'html.parser')
    # print(soup.prettify())

    print(soup.h1.a.text)




if __name__ == '__main__':
    main()