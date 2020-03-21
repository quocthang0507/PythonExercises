# Hãy tính tích các chữ số của số nguyên dương n

from Ex22 import Product


def ProductOfDigit(n):
    return Product([int(i) for i in str(n) if int(i) > 0])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Product digit of {}: '.format(n), ProductOfDigit(n))
