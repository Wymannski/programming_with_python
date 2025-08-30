def insert_ord(items:list[int],val:int)->list[int]:
    if not items:
        items.insert(0, val)
        return items
    idx = 0
    for item in items:
        if val < item:
            break
        idx += 1
    items.insert(idx,val)
    return items


if __name__ == '__main__':
    items = [1,2,3,5]
    print(insert_ord(items,4))
    print(insert_ord([],3))
    pass