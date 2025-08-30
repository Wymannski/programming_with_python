def reverse_list(items):
    for index, item in enumerate(items):
        if index < len(items) /2:
            temp = items[(-1)*(index+1)]
            items[(-1)*(index+1)] = items[index]
            items[index] = temp
    return items

def reverse_list_recursive(items):
    if not items:
        return items
    else:
        return reverse_list_recursive(items[1:]) + [items[0]]

print(reverse_list([1,2,3,4,5]))
print(reverse_list([1,2,3,4]))

print(reverse_list_recursive([1,2,3,4,5]))
print(reverse_list_recursive([1,2,3,4]))