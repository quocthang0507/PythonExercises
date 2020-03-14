# Đếm số lượng “ước số chẵn” của số nguyên dương n

from Ex25 import EvenDivisor
from Ex23 import Count


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = EvenDivisor(n)
    print('Even Divisor(s) of {}: '.format(n), a)
    print('Count: ', Count(a))
