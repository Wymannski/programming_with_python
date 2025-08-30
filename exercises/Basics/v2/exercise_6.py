from exercise_5 import insert_ord

def insertion_sort(items:list[int])->list[int]:
    res = []
    for item in items:
        insert_ord(res,item)
    return res

if __name__ == '__main__':
    items = [4,8,1,3,7]
    print(insertion_sort(items))
    pass