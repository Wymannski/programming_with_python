def generator_fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b, a + b

def rec_fibonacci(n:int):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return rec_fibonacci(n-2) + rec_fibonacci(n-1)

def generator_fibonacci_recursive():
    n = 0
    while True:
        yield rec_fibonacci(n)
        n += 1

def fibonacci():
    f1 = 0
    f2 = 1
    yield f1
    yield f2
    while True:
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3


def main():
    generator = generator_fibonacci()
    for _ in range(10):
        print(next(generator))

    generator_rec = generator_fibonacci_recursive()
    for _ in range(10):
        print(next(generator_rec))

    fibonacci_gen = fibonacci()
    for _ in range(10):
        print(next(fibonacci_gen))


if __name__ == '__main__':
    main()