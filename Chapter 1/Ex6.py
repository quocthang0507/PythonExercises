# Tính S(n) = 1/(1x2) + 1/(2x3) + … + 1/(𝑛x(𝑛+1))


def S(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(i*(i+1))
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
