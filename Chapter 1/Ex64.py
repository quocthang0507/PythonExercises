# 64. Giải phương trình 𝑎𝑥 + 𝑏 = 0.

if __name__ == "__main__":
    while True:
        a = eval(input("Nhap a = "))
        b = eval(input("Nhap b = "))
        if a != 0:
            break
    x = -b / a
    print("Nghiem cua phuong trinh {}𝑥 + {} = 0 la {}".format(a, b, x))
