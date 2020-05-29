# 56. Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không?


def isOnlyOdd(n):
    for c in str(n):
        if int(c) % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    if isOnlyOdd(n):
        print('This positive number has only odd digits')
    else:
        print('This positive number has not only odd digits')
