# Tính S(n) = 𝑥 + 𝑥^2/(2!) + 𝑥^3/(3!) + … + 𝑥^𝑛/(𝑛!)

from Ex9 import T as Factorial
from Ex10 import T as Power


def S(x, n):
    s = 0
    for i in range(1, n+1):
        s += Power(x, n)/Factorial(n)
    return s


if __name__ == "__main__":
    x = eval(input('x = '))
    n = eval(input('n = '))
    print('S(x, n) = ', S(x, n))
