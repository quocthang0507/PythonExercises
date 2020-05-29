# 62. Cho hai số nguyên dương a và b. Hãy vẽ lưu đồ tìm ước chung lớn nhất của hai giá trị này.
# greatest common multiple (gcm)
# greatest common divisor (gcd)
# greatest common factor (gcf)
# highest common factor (hcf)
# greatest common measure


def GCM(a, b):
    return GCM(b, a % b) if a % b > 0 else b


if __name__ == "__main__":
    while True:
        a = int(input('a = '))
        b = int(input('b = '))
        if a > 0 and b > 0:
            break
    result = GCM(a, b)
    print('The greatest common multiple number of {} and {} is {}'.format(a, b, result))
