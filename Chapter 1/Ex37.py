# Tính S(n) = 𝑛√(𝑛 + 𝑛−1√(𝑛 − 1 + ... + 3√(3 + √2))) có n – 1 dấu căn

from math import sqrt


def nrt(n, x):
    return x**(1/n)


def S(n):
    s = sqrt(2)
    for i in range(3, n+1):
        s = nrt(i, i+s)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    print('S(n) = ', S(n))
