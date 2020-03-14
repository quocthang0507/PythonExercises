# Tính tích tất cả “ước số lẻ” của số nguyên dương n

from Ex22 import Product
from Ex24 import OddDivisor


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = OddDivisor(n)
    print('Odd Divisor(s) of {}: '.format(n), a)
    print('Product: ', Product(a))
