# Tính S(n) = 1/(1/(1+1/(1+1/(1+1)))) có n dấu phân số


def S(n):
    s = 1/2
    for i in range(2, n+1):
        s = 1/(1+s)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('S(n) = ', S(n))
