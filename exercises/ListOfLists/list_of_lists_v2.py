def flat_list_of_list(items: list[list[int]]) -> list[int]:
    if not items:
        return []
    return items[0] + flat_list_of_list(items[1:])


def main():
    list_of_lists = [[3, 4, 5], [10, 4], [], [6, 12, 4]]

    print(flat_list_of_list(list_of_lists))


if __name__ == '__main__':
    main()
