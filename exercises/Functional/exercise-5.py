def generator_fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b


def get_fibonacci(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return get_fibonacci(n-1) + get_fibonacci(n-2)

def generator_fibonacci_recursive():
    n = 0
    while True:
        yield get_fibonacci(n)
        n += 1

def main():
    generator = generator_fibonacci()
    for _ in range(10):
       print(next(generator))

    generator_recursive = generator_fibonacci_recursive()
    for _ in range(10):
        print(next(generator_recursive))

if __name__ == '__main__':
   main()