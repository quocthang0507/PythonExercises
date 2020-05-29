# 55. Hãy đêm số lượng chữ số đầu tiên của số nguyên dương n.

if __name__ == "__main__":
    while True:
        n = int(input('n = '))
        if n > 0:
            break
    string = str(n)
    count = string.count(string[0])
    print('There are {} first digit in {}'.format(count, string))
