class MyRange:
    def __init__(self,n:int):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
       if self.current >= self.n:
           raise StopIteration
       self.current += 1
       return self.current-1


def main():
    my_range = MyRange(5)
    for item in my_range:
        print(item)

if __name__ == "__main__":
    main()