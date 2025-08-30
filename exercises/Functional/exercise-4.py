def generate_int():
    n = 0
    while True:
        yield n
        n += 1

def main():
    generator =generate_int()
    for item in range(10):
        print(next(generator))


if __name__ == '__main__':
    main()