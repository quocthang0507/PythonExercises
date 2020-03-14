# Tính S(n) = √(𝑥^n + √(𝑥^(n−1) + √(𝑥^(n−2) + ⋯ + √(𝑥^2 + √𝑥)))) có n dấu căn

from math import pow
from math import sqrt


def S(x, n):
    s = sqrt(x)
    for i in range(2, n+1):
        s = sqrt(pow(x, i) + s)
    return s


if __name__ == "__main__":
    while True:
        x = eval(input('x = '))
        n = eval(input('n = '))
        if n > 0:
            break
    print('S(x, n) = ', S(x, n))
