# Tính S(n) = 1/2 + 1/4 + + … + 1/2𝑛


def S(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(2*i)
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
