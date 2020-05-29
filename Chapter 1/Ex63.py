# 63. Cho hai số nguyên dương a và b. Hãy vẽ lưu đồ tìm bội chung nhỏ nhất của hai giá trị này.
# least common multiple
# lowest common multiple (LCM)
# smallest common multiple

from Ex62 import GCM


def LCM(a, b):
    return int(a * b / GCM(a, b))


if __name__ == "__main__":
    while True:
        a = int(input('a = '))
        b = int(input('b = '))
        if a > 0 and b > 0:
            break
    result = LCM(a, b)
    print('The least common multiple number of {} and {} is {}'.format(a, b, result))
