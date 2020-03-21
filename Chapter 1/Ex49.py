# Cho số nguyên dương n. Hãy tìm chữ số đầu tiên của n


def FindFirstDigit(n):
    return int(str(n)[0])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('First digit of {}: '.format(n), FindFirstDigit(n))
