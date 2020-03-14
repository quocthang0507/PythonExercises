# Tính T(x, n) = 𝑥^𝑛


def T(x, n):
    return x**n


def T_2(x, n):
    t = x
    for i in range(2, n+1):
        t *= x
    return t


if __name__ == "__main__":
    x = eval(input('x = '))
    n = eval(input('n = '))
    print('T(n) = ', T(x, n))
    print('T_2(n) = ', T_2(x, n))
