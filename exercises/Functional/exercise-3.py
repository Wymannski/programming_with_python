class Cycle:
    def __init__(self,iterable):
        self.iterableInput = iterable
        self.iterable = iter(iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable,None)
        if value:
            return value
        else:
            self.iterable = iter(self.iterableInput)
            return next(self.iterable)


def main():
    items = [1,2,3,4]
    cycle = Cycle(items)
    for _ in range(10):
        print(next(cycle))

if __name__ == '__main__':
    main()