# Tính S(n) = 1 + 1x2 + 1x2x3 + ⋯ + 1x2x3x … x𝑛

from Ex9 import T as Factorial


def S(n):
    s = 0
    for i in range(1, n+1):
        s += Factorial(i)
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
