class ListIter:
    def __init__(self,lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
           raise StopIteration
        self.index +=1
        return self.lst[self.index-1]



def main():
    l = ListIter([2,5,7])
    for x in l:
        print(x)


if __name__ == '__main__':
    main()