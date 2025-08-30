from operator import index


class MyRange:
    def __init__(self,n):
        self.n = n
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.n:
            raise StopIteration()
        val = self.value
        self.value += 1
        return val




def main():
    range = MyRange(5)
    for i in range:
        print(i)

if __name__ == '__main__':
    main()