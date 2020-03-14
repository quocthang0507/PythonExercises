# Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó

from Ex20 import Divisor


def SumLess(a, n):
    s = 0
    for i in a:
        if i < n:
            s += i
    return s


def SumLess_2(a, n):
    return sum(i for i in a if i < n)


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = Divisor(n)
    print('Divisor(s) of {}: '.format(n), a)
    print('Sum less than {}: '.format(n), SumLess(a, n))
    print('Sum less than {}: '.format(n), SumLess_2(a, n))
    print('Sum less than {}: '.format(n), sum(a[:-1]))
