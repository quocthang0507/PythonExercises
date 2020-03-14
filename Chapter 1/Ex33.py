# Tính S(n) = √(2 + √(2 + √(2 + ⋯ + √(2 + √2)))) có n dấu căn

from math import sqrt


def S(n):
    s = sqrt(2)
    for i in range(0, n-1):
        s = sqrt(2+s)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    print('S(n) = ', S(n))
