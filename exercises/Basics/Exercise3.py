def get_max_value(items):
    max_value = 0
    for item in items:
        if item > max_value:
            max_value = item
    return max_value

print(get_max_value([1,2,3]))