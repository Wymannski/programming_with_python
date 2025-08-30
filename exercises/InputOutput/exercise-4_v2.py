import re


def word_of_length_2(string:str):
    return re.findall(r'[A-Z]\w+',string)

def email_addresses(string:str):
    return re.findall(r'\w+\.\w+@\w+\.\w+',string)

def main():
    try:
        with open('email-addresses.txt','r',encoding='UTF-8') as file:
            content = file.read()
    except FileNotFoundError:
        print('file not found')

    print(word_of_length_2(content))
    print(email_addresses(content))



if __name__ == '__main__':
    main()