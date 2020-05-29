# 61. Hãy kiểm tra các chữ số của số nguyên dương n có giảm dần từ trái sang phải hay không?


def isDescending(n):
    string = str(n)
    for i in range(len(string)-1):
        if string[i] <= string[i+1]:
            return False
    return True


if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    if isDescending(n):
        print('This positive number is descending')
    else:
        print('This positive number is not descending')
