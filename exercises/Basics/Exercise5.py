def insert_number(items:list[int], number:int) :
    if len(items) == 0:
        items.append(number)
        return items

    for index in range(len(items)):
        if number < items[index]:
            items.insert(index,number)
            break
        if index == len(items)-1:
            items.append(number)
    return items





print(insert_number([1,2,4],3))
print(insert_number([1,2,4],5))
