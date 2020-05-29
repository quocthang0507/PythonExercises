# 59. Hãy kiểm tra số nguyên dương n có phải số đối xứng hay không?


def isSymmetrical(n):
    string = str(n)
    l = len(string)
    mid = int(l/2)
    for i in range(0, mid):
        if string[i] != string[l-i-1]:
            return False
    return True


if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    if isSymmetrical(n):
        print('This positive number is symmetrical')
    else:
        print('This positive number is asymmetrical')
