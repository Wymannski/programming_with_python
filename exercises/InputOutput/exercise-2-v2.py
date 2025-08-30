import sys


def main():
    file_one = sys.argv[1]
    file_two = sys.argv[2]

    try:
        with open(file_one, 'r', encoding='UTF-8') as file:
            data1 = file.read()
    except FileNotFoundError:
        print('file1 not found')
        exit()

    try:
        with open(file_two, 'r', encoding='UTF-8') as file:
            data2 = file.read()
    except FileNotFoundError:
        print('file2 not found')
        exit()

    try:
        with open('results2.txt', 'a', encoding='UTF-8') as file:
           file.write(data1)
           file.write(data2)
    except FileNotFoundError:
        print('file1 not found')
        exit()




if __name__ == '__main__':
    main()
