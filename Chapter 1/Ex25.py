# Tính tổng tất cả “ước số chẵn” của số nguyên dương n

from Ex21 import Sum


def EvenDivisor(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            a.append(i)
    return a


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = EvenDivisor(n)
    print('Even Divisor(s) of {}: '.format(n), a)
    print('Sum: ', Sum(a))
