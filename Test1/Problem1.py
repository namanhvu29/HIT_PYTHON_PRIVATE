import math
def giaiThua(n):
    if n < 0:
        return "Khong xac dinh"
    elif n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range (1, n+1):
            res = res * i
        return res


x = int(input("nhap so x: "))
ham_e = 0
n = int(input("nhap so n: "))
for n in range (0, n):
    tu_so = x ** n
    mau_so = giaiThua(n)
    so_hien_tai = tu_so / mau_so
    ham_e = ham_e + so_hien_tai
print("ket qua: ", ham_e)
