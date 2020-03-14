# Tính tích tất cả “ước số” của số nguyên dương n

from Ex20 import Divisor


def Product(a):
    p = 1
    for n in a:
        p *= n
    return p


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = Divisor(n)
    print('Divisor(s) of {}: '.format(n), a)
    print('Product of divisors: ', Product(a))
