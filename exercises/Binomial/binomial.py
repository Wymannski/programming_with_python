def binomial_rec(n: int, k: int):
    if k == 0 or n == k:
        return 1
    return binomial_rec(n -1,k) + binomial_rec(n-1,k-1)

def binomial_real(n: float,k: float)-> float:
    if k == 0.0:
        return 1.0
    else:
        return n/k * binomial_real(n-1,k-1)

def main():
    print(binomial_rec(3,2))
    print(binomial_real(3.0,2.0))

if __name__ == '__main__':
    main()