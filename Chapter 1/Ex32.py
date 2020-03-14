# Cho số nguyên dương n. Kiểm tra số nguyên dương n có phải
# là số chính phương hay không

# Số chính phương hay còn gọi là số hình vuông là số tự nhiên
# có căn bậc 2 là một số tự nhiên, hay nói cách khác, số chính
# phương là bình phương (lũy thừa bậc 2) của một số tự nhiên.

from Ex10 import T as Power
import math


def IsSquare(n):
    for i in range(1, int(math.sqrt(n))+1):
        if Power(i, 2) == n:
            return True
    return False


def IsSquare_2(n):
    return Power(n, 1/2) == int(Power(n, 1/2))


if __name__ == "__main__":
    while True:
        n = eval(input('N = '))
        if n > 0:
            break
    if IsSquare(n):
        print('{} is square number'.format(n))
    else:
        print('{} is not square number'.format(n))
    if IsSquare_2(n):
        print('{} is square number'.format(n))
    else:
        print('{} is not square number'.format(n))
