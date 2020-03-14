# Tính S(n) = 𝑥 + 𝑥^3/(3!) + 𝑥^5/(5!) + … + (𝑥^(2𝑛+1))/((2n+1)!)

from Ex9 import T as Factorial
from Ex10 import T as Power


def S(x, n):
    s = 0
    for i in range(0, n):
        s += Power(x, 2*n+1)/Factorial(2*n+1)
    return s


if __name__ == "__main__":
    x = eval(input('x = '))
    n = eval(input('n = '))
    print('S(x, n) = ', S(x, n))
