# Cho n là số nguyên dương. Hãy tìm giá trị nguyên dương k lớn nhất sao
# cho S(k) < n. Trong đó chuỗi S(k) được định nghĩa như sau : S(k) = 1 +
# 2 + 3 + … + k

from Ex1 import S as Sum


def FindK(n):
    k = 1
    for i in range(1, n+1):
        if Sum(i) < n:
            k = i
        else:
            break
    return k


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Max k = ', FindK(n))
