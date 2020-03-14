# Tính S(n) = 1 + 1/(1+2) + 1/(1+2+3) + … + 1/(1+2+3+⋯+𝑛)

from Ex1 import S as Sum


def S(n):
    s = 0
    for i in range(1, n+1):
        s += 1/Sum(i)
    return s


def S_2(x, n):
    s = 0
    for i in range(1, n+1):
        s += x/Sum(i)
    return s


def S_3(x, n):
    s = 0
    for i in range(1, n+1):
        s += (x**i)/Sum(i)
    return s


if __name__ == "__main__":
    n = eval(input('n = '))
    print('S(n) = ', S(n))
    print('S_2(n) = ', S_2(1, n))
    print('S_3(n) = ', S_3(1, n))
