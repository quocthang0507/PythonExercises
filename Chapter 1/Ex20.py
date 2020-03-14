# Liệt kê tất cả “ước số” của số nguyên dương n


def Divisor(n):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    return d


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    print('Divisor(s) of {}: '.format(n), Divisor(n))
