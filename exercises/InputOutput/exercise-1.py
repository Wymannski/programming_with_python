

def main():
    try:
        with open('./email-addresses.txt') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("File does not exist")

    words= 0
    characters = 0
    lines = 0
    for character in file_data:
        if character == ' ':
            words +=1

        if character == '\n':
            lines += 1

        characters +=1

    print(words)
    print(characters)
    print(lines)


if __name__ == '__main__':
    main()