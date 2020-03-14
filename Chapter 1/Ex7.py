# Tính S(n) = 1/2 + 2/3 + 3/4 + … + 𝑛/(𝑛+1)


def S(n):
    s = 0
    for i in range(1, n+1):
        s += i/(i+1)
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
