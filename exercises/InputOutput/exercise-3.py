import re

def contains_vowel(input:str)-> bool:
    match = re.match("^.*[aeiou].*$",input)
    return True if match else False

def represents_integer(input:str)-> bool:
    match = re.match("^[1-9][0-9]*$",input)
    return True if match else False

def represents_date(input:str)-> bool:
    match = re.match("^[0-9]{4}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$",input)
    return True if match else False


def main():
    if contains_vowel("Spain"):
        print("Spain contains vowel")
    if not contains_vowel("T"):
        print("T does not contain vowel")

    if represents_integer("100000"):
        print("100000 represents integer")

    if not represents_integer("0100000"):
        print("0100000 does not represent an integer")

    if represents_date("2003-12-14"):
        print("2003-12-14 represents date")

    if not represents_date("2003-12-44"):
        print("2003-12-44 does not represent date")




if __name__ == '__main__':
    main()