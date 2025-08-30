def binomial_rec(n:int,k:int)->int:
    if k > n:
        return 0
    if k == n or k == 0:
        return 1
    return binomial_rec(n-1,k) + binomial_rec(n-1,k-1)


def main():
    print(binomial_rec(4,2))

if __name__ == '__main__':
    main()