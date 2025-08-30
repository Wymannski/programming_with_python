def list_len(word_list):
    result = []
    for items in word_list:
        length = 0
        for item in items:
            length += 1
        result.append(length)
    return result

print(list_len(["abc","de","fghi"]))


