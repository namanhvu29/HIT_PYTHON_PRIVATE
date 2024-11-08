def tao_matran_tu_list(a, n, m):
    k = len(a)
    if k < n * m:
        return "Khong tao duoc ma tran do khong du phan tu"
    matran = []
    for i in range(n):
        dong = a[i * m:(i + 1) * m]
        matran.append(dong)
    return matran

k = int(input("Nhap so phan tu trong mang: "))
a = [int(input("Nhap phan tu"))  for i in range (0, k)]
n = int(input("Nhap cot: "))
m = int(input("Nhap dong: "))



ketqua = tao_matran_tu_list(a, n, m)
if isinstance(ketqua, str):
    print(ketqua)
else:
    print("[", end=" ")
    for row in ketqua:
        print(f"[ {', '.join(map(str, row))} ]", end=" , " if row != ketqua[-1] else "")
    print("]")
