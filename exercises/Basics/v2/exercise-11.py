from exercise_10 import to_binary_dict
def int_to_bin_8(items:list[int])->list[list[bool]]:
    return list(map(to_binary_dict,items))

if __name__ == '__main__':
    integers = [1,2,3]
    print(int_to_bin_8(integers))
    pass