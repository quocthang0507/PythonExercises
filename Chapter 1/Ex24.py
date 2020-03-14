# Liệt kê tất cả “ước số lẻ” của số nguyên dương


def OddDivisor(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            a.append(i)
    return a


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = OddDivisor(n)
    print('Odd Divisor(s) of {}: '.format(n), a)
