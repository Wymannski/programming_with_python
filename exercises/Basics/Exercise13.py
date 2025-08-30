def remove_outliers(dictionary: dict)-> dict:
    max_value = 0
    max_key = ''
    min_value = 1000000
    min_key = ''
    for k,v in dictionary.items():
        if max_value < v:
            max_value = v
            max_key = k
        if min_value > v:
            min_value = v
            min_key = k
    dictionary.pop(max_key)
    dictionary.pop(min_key)
    return dictionary

print(remove_outliers({'a':1,'b':2,'c':3,'d':4,}))
