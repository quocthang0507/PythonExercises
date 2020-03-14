# Tính S(n) = √(1 + √(2 + √(3+ ⋯ + √(𝑛−1 + √𝑛)))) có n dấu căn

from math import sqrt


def S(n):
    s = sqrt(n)
    for i in range(n-1, 0,-1): # n-1..1
        s = sqrt(i+s)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    print('S(n) = ', S(n))
