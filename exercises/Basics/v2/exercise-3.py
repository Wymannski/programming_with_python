def max_val(items:list[float])->float:
    max_val = 0
    for item in items:
        if item > max_val:
            max_val = item
    return max_val

if __name__ == '__main__':
    print(max_val([1,2,3]))