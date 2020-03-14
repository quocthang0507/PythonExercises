# Hãy đếm số lượng chữ số của số nguyên dương n


def Len(n):
    return len(str(n))


def Len_2(n):
    l = 0
    while n > 0:
        l += 1
        n = int(n/10)
    return l


if __name__ == "__main__":
    while True:
        n = eval(input('n = '))
        if n > 0:
            break
    print('Length of {}: '.format(n), Len(n))
    print('Length of {}: '.format(n), Len_2(n))
