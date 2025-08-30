"""A simple program that sums up numbers."""


def sum_up(max_num):
    """Returns the sum of numbers from 1 up and including max_num."""
    accumulator = 0
    for i in range(1, max_num + 1):
        accumulator += i
    return accumulator


def main():
    """Invokes sumup and prints the result."""
    max_num = 100
    the_sum = sum_up(max_num)
    print('sum of 1 to {} is {}.'.format(max_num, the_sum))


if __name__ == '__main__':
    main()
