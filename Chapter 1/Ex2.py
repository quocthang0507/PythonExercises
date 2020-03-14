# Tính S(n) = 1^2 + 2^2 + 3^2 + … + n^2


def S(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
