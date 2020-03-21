# Tìm chữ số lớn nhất của số nguyên dương n


def MaxDigit(n):
    return max(str(n))


def MaxDigit_2(n):
    s = str(n)
    max = int(s[0])
    for c in s[1:]:
        if max < int(c):
            max = int(c)
    return max


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Max digit of {}: '.format(n), MaxDigit(n))
    print('Max digit of {}: '.format(n), MaxDigit_2(n))
