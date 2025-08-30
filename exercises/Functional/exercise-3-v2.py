class Cycle:
    def __init__(self,iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)


    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator,None)
        if value:
            return value
        else:
            self.iterator = iter(self.iterable)
            return next(self.iterator)




def main():
    items = [1,2,3,4]
    cycle = Cycle(items)
    for _ in range(10):
        print(next(cycle))

if __name__ == '__main__':
    main()