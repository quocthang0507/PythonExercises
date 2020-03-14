# Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2𝑛+1)


def S(n):
    s = 0
    for i in range(0, n):
        s += 1/(2*i+1)
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
