# Hãy đếm số lượng chữ số lẻ của số nguyên dương n


def CountOdd(n):
    c = 0
    for i in str(n):
        if int(i) % 2 != 0:
            c += 1
    return c


def CountOdd_2(n):
    return len([i for i in str(n) if int(i) % 2 != 0])


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Count odd digit of {}: '.format(n), CountOdd(n))
    print('Count odd digit of {}: '.format(n), CountOdd_2(n))
