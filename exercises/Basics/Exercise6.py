import Exercise5 as Insert
def insertion_sort(items):
    sorted_list = []
    for item in items:
        sorted_list = Insert.insert_number(sorted_list, item)
    return sorted_list



print(insertion_sort([4,2,3,1]))
