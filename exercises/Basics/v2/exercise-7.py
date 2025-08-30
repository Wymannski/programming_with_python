def sum_ints(items:list[int])->list[int]:
    sum = 0
    for item in items:
        sum += item
    return sum

def sum_rec(items:list[int])->int:
    if not items:
        return 0
    return items[0] + sum_rec(items[1:])




if __name__ == '__main__':
    items = [1,2,3,4]
    print(sum_ints(items))
    print(sum_rec(items))
    pass