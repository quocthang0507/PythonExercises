# 54. Hãy đếm số lượng chữ số nhỏ nhất của số nguyên dương n.

from Ex52 import MinDigit

if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    count = str(n).count(MinDigit(n))
    print('There are {} min digits in {}'.format(count, n))
