import sys

def dict_min_max(dictionary:dict)->dict:
    result = {}
    min = sys.maxsize
    key_min = ''
    max = 0
    key_max = ''
    for key,value in dictionary.items():
        if value > max:
            max = value
            key_max = key
        if value < min:
            min = value
            key_min = key
    dictionary.pop(key_max)
    dictionary.pop(key_min)
    return dictionary

if __name__ == '__main__':
    dictionary = {'a':1,'b':2,'c':3,'d':4}
    print(dict_min_max(dictionary))
    pass