def sum_list(list: list[int]) -> int:
    sum = 0
    for item in list:
        sum += item
    return sum

def recursive_sum_list(integer_list: list[int]) -> int:
    if len(integer_list) > 0:
        return integer_list[0] + recursive_sum_list(integer_list[1:])
    else:
        return 0

print(sum_list([1,2,3]))
print(recursive_sum_list([1,2,3]))