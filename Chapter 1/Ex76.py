# 76. Kiểm tra số nguyên 4 byte có dạng 3^𝑘 hay không?

import math


def KT_1(n):
    t = 1
    for i in range(1, n):
        t *= 3
        if t == n:
            return i
        elif t > n:
            return -1


def KT_2(n):
    i = 0
    while n != 1:
        if n % 3 == 0:
            n /= 3
            i += 1
        else:
            return -1
    return i


if __name__ == "__main__":
    try:
        n = int(input("Nhap n = "))
        result = KT_2(n)
        if result != -1:
            print("3^{} = {}".format(result, n))
        else:
            print("Khong phai")
    except:
        print("So ban nhap khong phai la so nguyen")
