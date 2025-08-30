def main():
    fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

    print(list(filter(lambda x: x.startswith('A'),fruit)))

if __name__ == '__main__':
    main()