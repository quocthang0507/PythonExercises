# 53. Hãy đếm số lượng chữ số lớn nhất của số nguyên dương n.

from Ex51 import MaxDigit

if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    count = str(n).count(MaxDigit(n))
    print('There are {} max digits in {}'.format(count, n))
