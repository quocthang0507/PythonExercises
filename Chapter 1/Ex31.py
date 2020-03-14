# Cho số nguyên dương n. Kiểm tra số nguyên dương n có phải
# là số nguyên tố hay không

from Ex20 import Divisor
from Ex23 import Count
import math


def IsPrime(n):
    return Count(Divisor(n)[1:-1]) == 0


def IsPrime_2(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    if IsPrime(n):
        print('{} is prime number'.format(n))
    else:
        print('{} is not prime number'.format(n))
    if IsPrime_2(n):
        print('{} is prime number'.format(n))
    else:
        print('{} is not prime number'.format(n))
