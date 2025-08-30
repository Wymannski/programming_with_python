def flat(list_of_lists: list[list]) -> list:
    result = []
    for list_of_items in list_of_lists:
        for item in list_of_items:
            result.append(item)
    return result

print(flat([[3,8],[8,9,9],[1,2]]))
print(flat([["ab","c"],["d","ef"]]))
