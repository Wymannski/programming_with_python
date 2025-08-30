import requests
from bs4 import BeautifulSoup


def main():
    base_url = 'https://quotes.toscrape.com/'
    response = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(response.content, 'html.parser')

    dictionary = {}

    authors = soup.find_all('small', attrs={'class': 'author'})

    for author in authors:
        if author.text in dictionary.keys():
            dictionary[author.text] = dictionary[author.text] + 1
        else:
            dictionary[author.text] = 1
        # print(author.text)

    li = soup.find('li', attrs={'class': 'next'})
    if li is not None:
        next_link = li.a['href']
        print(next_link)

    while next_link is not None:
        response = requests.get(base_url + next_link)
        soup = BeautifulSoup(response.content, 'html.parser')
        li = soup.find('li', attrs={'class': 'next'})
        if li is not None:
            next_link = li.a['href']
            print(next_link)

            authors = soup.find_all('small', attrs={'class': 'author'})

            for author in authors:
                if author.text in dictionary.keys():
                    dictionary[author.text] = dictionary[author.text] + 1
                else:
                    dictionary[author.text] = 1
                # print(author.text)
        else:
            next_link = None

    for key,value in dictionary.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
