# Hãy tính tổng các chữ số chẵn của số nguyên dương n


def SumEven(n):
    return sum([int(i) for i in str(n) if int(i) % 2 == 0])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Sum even digit of {}: '.format(n), SumEven(n))
