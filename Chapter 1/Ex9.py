# Tính T(n) = 1 x 2 x 3 x … x 𝑛


def T(n):
    t = 1
    for i in range(2, n+1):
        t *= i
    return t


def T_2(n):
    if n == 1:
        return 1
    return n*T_2(n-1)


def T_3(n):
    return 1 if n == 1 else n*T_2(n-1)


if __name__ == "__main__":
    n = eval(input('N = '))
    print('T(n) = ', T(n))
    print('T_2(n) = ', T_2(n))
    print('T_3(n) = ', T_3(n))