n = int(input("Nhap so phan tu cua A: "))
A = tuple(int(input(f"Nhap phan tu thu {i + 1} cua A: ")) for i in range(n))
print(f"Tuple A: {A}")

m = int(input("Nhap so phan tu cua B: "))
B = tuple(input(f"Nhap phan tu thu {i + 1} cua B: ") for i in range(m))
print(f"Tuple B: {B}")

trungBinhA = sum(A) / len(A)
soLonHonTrungBinh = sum(1 for x in A if x > trungBinhA)
print(f"So luong phan tu trong A lon hon trung binh cong la: {soLonHonTrungBinh}")

chan = tuple(x for x in A if x % 2 == 0)
le = tuple(x for x in A if x % 2 != 0)
print(f"Tuple cac so chan: {chan}")
print(f"Tuple cac so le: {le}")

k = input("Nhap ki tu k: ")
demK = B.count(k)
print(f"So lan xuat hien '{k}' trong B: {demK}")

kitu = tuple(s for s in B if len(s) >= 5)
print(f"Cac phan tu trong B co do dai >= 5 ki tu: {kitu}")

toithieu = min(len(A), len(B))
C = tuple((A[i], B[i]) for i in range(toithieu))
print(f"Tuple moi C sau khi ghep cap: {C}")
