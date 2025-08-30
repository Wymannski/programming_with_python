import Exercise10 as BinaryConverter
def to_list_of_binary(items: list[int]) -> list[list[bool]]:
    result = []
    for item in items:
        result.append(BinaryConverter.to_binary(item))
    return result

print(to_list_of_binary([1,2,3]))
