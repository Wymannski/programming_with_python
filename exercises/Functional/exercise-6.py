

def main():
    fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

    print(list(filter(lambda x:x[0] == 'A',fruit)))

if __name__ == '__main__':
    main()