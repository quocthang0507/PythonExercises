# Tính S(n) = 𝑥 + 𝑥^2/(1+2) + 𝑥^3/(1+2+3) + … + 𝑥^𝑛/(1+2+3+⋯+𝑛)

from Ex15 import S_3 as Sum


def S(x, n):
    return Sum(x, n)


if __name__ == "__main__":
    x = eval(input('x = '))
    n = eval(input('n = '))
    print('S(x, n) = ', S(x, n))
