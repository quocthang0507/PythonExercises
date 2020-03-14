# Tính tổng tất cả “ước số” của số nguyên dương n

from Ex20 import Divisor


def Sum(a):
    s = 0
    for n in a:
        s += n
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = Divisor(n)
    print('Divisor(s) of {}: '.format(n), a)
    print('Sum of divisors: ', Sum(a))
    print('Sum of divisors: ', sum(a))
