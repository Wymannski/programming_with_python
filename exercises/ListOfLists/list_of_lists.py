def flatten_list(list : list[list[int]])-> list[int]:
    if not list: return []
    return list[0] + flatten_list(list[1:])



def main():
    elements = [[3,4,5],[10,4],[6,12,4]]
    print(flatten_list(elements))


if __name__ == '__main__':
    main()