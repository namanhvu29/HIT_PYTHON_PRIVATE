def TimSoChung(num_list1, num_list2):
    ketqua = []
    dem = {}
    for num in num_list1:
        dem[num] = dem.get(num, 0) + 1

    for num in num_list2:
        if num in dem and dem[num] > 0:
            ketqua.append(num)
            dem[num] -= 1
    return ketqua

n = int(input("Nhap so phan tu trong mang num1: "))
num1 = [input("Nhap cac phan tu trong mang num1:") for i in range(0, n)]
m = int(input("Nhap so phan tu trong mang num2: "))
num2 = [input("Nhap cac phan tu trong mang num2:") for i in range(0, m)]
print("Mang so chung:", TimSoChung(num1, num2))

