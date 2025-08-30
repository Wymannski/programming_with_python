def reverse(items: list) -> list:
    for idx,item in enumerate(items):
        if idx < (len(items)/2):
            items[idx] = items[len(items)-1-idx]
            items[len(items)-1-idx] = item
    return items

def revers_rec(items: list) -> list:
    if not items:
        return []
    return [items[len(items)-1]] + revers_rec(items[:len(items)-1])

if __name__ == '__main__':
    items = [3,1,2,4,5]
    print(reverse(items))
    items = [3,1,2,4,5]
    print(revers_rec(items))
