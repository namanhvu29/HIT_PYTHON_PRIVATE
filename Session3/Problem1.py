#1.
def giaithua(n):
    res = 1
    for n in range(1, n + 1):
        res = res * n
    return res

def ham(x):
    hamE = 0
    for n in range (0, 999):
        hamE = hamE + ((x**n)/giaithua(n))
    return hamE

# 2.
def sum():
    n = int(input("Nhap so n:"))
    sum = 0
    for i in range (0, n + 1):
        sum = sum + (1/giaithua(n))
    print("Gia tri cua tong S la ", sum)

x = 2
ham(x)
sum()