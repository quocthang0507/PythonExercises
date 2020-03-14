# Cho số nguyên dương n. Kiểm tra số dương n có phải là số
# hoàn thiện hay không

# Số hoàn thiện (hay còn gọi là số hoàn chỉnh, số hoàn hảo
# hoặc số hoàn thành) là một số nguyên dương mà tổng các ước
# nguyên dương chính thức của nó (số nguyên dương bị nó chia
# hết ngoại trừ nó) bằng chính nó.

from Ex20 import Divisor
from Ex21 import Sum


def IsPerfect(n):
    return Sum(Divisor(n)[:-1]) == n


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    if IsPerfect(n):
        print('{} is perfect number'.format(n))
    else:
        print('{} is not perfect number'.format(n))
