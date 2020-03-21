# Hãy tìm chữ số đảo ngược của số nguyên dương n


def ReverseDigit(n):
    return int(str(n)[::-1])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Reversing digit of {}: '.format(n), ReverseDigit(n))
