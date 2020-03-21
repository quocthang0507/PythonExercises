# Hãy tính tích các chữ số lẻ của số nguyên dương n

from Ex22 import Product


def ProductOdd(n):
    return Product([int(i) for i in str(n) if int(i) % 2 != 0])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Product odd digit of {}: '.format(n), ProductOdd(n))
