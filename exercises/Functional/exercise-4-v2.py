def integer_generator():
    a = 0
    while True:
        yield a
        a += 1


def main():
    generator = integer_generator()
    for _ in range(10):
        print(next(generator))

if __name__ == '__main__':
    main()
