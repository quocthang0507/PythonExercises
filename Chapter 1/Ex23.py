# Đếm số lượng “ước số” của số nguyên dương n

from Ex20 import Divisor


def Count(a):
    c = 0
    for n in a:
        c += 1
    return c


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = Divisor(n)
    print('Divisor(s) of {}: '.format(n), a)
    print('There are {} divisors'.format(Count(a)))
    print('There are {} divisors'.format(len(a)))
