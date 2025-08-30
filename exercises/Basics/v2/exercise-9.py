def flat(items:list[list])->list:
    if not items:
        return []
    return items[0] + flat(items[1:])

if __name__ == '__main__':
    integers =[[3,8],[8,9,9],[1,2]]
    print(flat(integers))
    strings = ["ab","c"],["d","ef"]
    print(flat(strings))
    pass