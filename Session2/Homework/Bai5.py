# a)
def bits():
    soThapPhan = int(input('Nhap so thap phan: '))
    soBatPhan = format(soThapPhan,'o')
    soBits = len(soBatPhan) * 3
    return f"So bits de bieu dien so thap phan {soThapPhan} o dang bat phan la {soBits}"

# Khi chay a thi bo comment dong 9,10
# bits = bits()
# print(bits)

# b)
def kiemtra():
    a = int(input("Nhap so a: "))
    b = dir(a)
    return b
# Khi chay b thi bo comment dong 18,19
# a = kiemtra()
# print(a)
