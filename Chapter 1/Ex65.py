# 65. Giải phương trình 𝑎𝑥^2 + 𝑏𝑥 + 𝑐 = 0.

import math


def GiaiPTBac2(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        raise Exception("Phuong trinh vo nghiem")
    elif delta == 0:
        return -b/(2*a)
    else:
        return -b + math.sqrt(delta)/(2 * a), -b - math.sqrt(delta)/(2 * a)


if __name__ == "__main__":
    while True:
        a = eval(input("Nhap a = "))
        b = eval(input("Nhap b = "))
        c = eval(input("Nhap c = "))
        if a != 0:
            break
    try:
        x = GiaiPTBac2(a, b, c)
        if len(x) == 1:
            print("Phuong trinh co nghiem kep: ", x)
        else:
            print(
                "Phuong trinh co hai nghiem phan biet x_1 = {} va x_2 = {}".format(x[0], x[1]))
    except:
        print("Phuong trinh vo nghiem")
