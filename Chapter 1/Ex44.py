# Hãy tính tổng các chữ số của số nguyên dương n


def SumOfDigit(n):
    return sum([int(i) for i in str(n)])


def SumOfDigit_2(n):
    s = 0
    while n > 0:
        s += n % 10
        n = int(n/10)
    return s


def SumOfDigit_3(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Length of {}: '.format(n), SumOfDigit(n))
    print('Length of {}: '.format(n), SumOfDigit_2(n))
    print('Length of {}: '.format(n), SumOfDigit_3(n))
