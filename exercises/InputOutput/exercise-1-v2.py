def main():
    try:
        with open('email-addresses.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found')

    if lines:
        line_count = 0
        word_count = 0
        character_count = 0
        for line in lines:
            line_count += 1
            for character in line:
                if character.isspace():
                    word_count += 1
                character_count +=1

        print('line count: ',line_count)
        print('word count: ', word_count)
        print('character count: ', character_count)


if __name__ == '__main__':
    main()
