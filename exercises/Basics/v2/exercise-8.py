def list_len(items: list[str]) -> list[int]:
    res = []
    for item in items:
        res.append(len(item))
    return res


if __name__ == '__main__':
    items: list[str] = ["abc", "de", "fghi"]
    print(list_len(items))
    pass
