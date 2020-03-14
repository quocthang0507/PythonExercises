# Tính S(n) = 1/2 + 3/4 + 5/6 + … + (2𝑛+1)/(2𝑛+2)


def S(n):
    s = 0
    for i in range(0, n):
        s += (2*i+1)/(2*i+2)
    return s


if __name__ == "__main__":
    n = eval(input('N = '))
    print('S(n) = ', S(n))
