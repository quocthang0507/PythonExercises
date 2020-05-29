# 57. Hãy kiểm tra số nguyên dương n có toàn chữ số chẵn hay không?


def isOnlyEven(n):
    for c in str(n):
        if int(c) % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    if isOnlyEven(n):
        print('This positive number has only even digits')
    else:
        print('This positive number has not only even digits')
