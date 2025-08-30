import re

def get_all_two_digits_words(input:str):
    return re.findall("[A-Z]{1}[a-zA-Z]{1,}",input)

def get_all_emails(input:str):
    return re.findall(r"[\w.]+@[\w]+.[\w]{2,4}",input)

def main():
    try:
        with open('./email-addresses.txt') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("File does not exist")
    if file_data:
        print(get_all_two_digits_words(file_data))
        print(get_all_emails(file_data))

if __name__ == '__main__':
    main()