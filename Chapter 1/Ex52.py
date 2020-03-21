# Tìm chữ số nhỏ nhất của số nguyên dương n


def MinDigit(n):
    return min(str(n))


def MinDigit_2(n):
    s = str(n)
    min = int(s[0])
    for c in s[1:]:
        if min > int(c):
            min = int(c)
    return min


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Min digit of {}: '.format(n), MinDigit(n))
    print('Min digit of {}: '.format(n), MinDigit_2(n))
