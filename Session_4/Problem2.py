def GhepMang(a, b):
    c = []
    c_lenght = max(len(a), len(b))
    for i in range(c_lenght):
        if i < len(a):
            c.append(a[i])
        if i < len(b):
            c.append(b[i])
    return c

n = int(input("Nhap so phan tu trong mang a: "))
a = [input("Nhap cac phan tu trong mang a:") for i in range(0, n)]
m = int(input("Nhap so phan tu trong mang b: "))
b = [input("Nhap cac phan tu trong mang b:") for i in range(0, m)]
c = GhepMang(a, b)
print("c = ", c)
