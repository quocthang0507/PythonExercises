# Tính S(n) = √(𝑛 + √(𝑛−1 + √(𝑛−2 + ⋯ + √(2 + √1)))) có n dấu căn

from math import sqrt


def S(n):
    s = sqrt(1)
    for i in range(2, n+1):
        s = sqrt(i+s)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    print('S(n) = ', S(n))
