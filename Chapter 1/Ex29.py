# Tìm ước số lẻ lớn nhất của số nguyên dương n.
# Ví dụ n = 100 ước lẻ lớn nhất của 100 là 25

from Ex24 import OddDivisor
from Ex20 import Divisor


def Max(a):
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
    return max


def Max_2(a):
    return Max([i for i in a if i % 2 != 0])


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    a = OddDivisor(n)
    print('Odd Divisor(s) of {}: '.format(n), a)
    print('Max: ', Max(a))
    print('Max: ', max(a))
    print('Max: ', Max_2(Divisor(n)))
    print('Max: ', a[-1])