import random

def taoTaiKhoan(n):
    prefixes = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
    taiKhoan = {}
    
    for i in range(1, n + 1):

        username = f"202360{str(i).zfill(4)}"

        password = f"{random.choice(prefixes)}{username}"

        taiKhoan[f"Account{i}"] = {
            "Username": username,
            "Password": password
        }
    
    return taiKhoan

n = int(input("Nhap so tai khoan can tao: "))
if 1 <= n <= 100:
    danhsachTK = taoTaiKhoan(n)

    for taiKhoan, thongTin in danhsachTK.items():
        print(f"{taiKhoan}: {thongTin}")
else:
    print("Soluong tai khoan 1 toi 100.")
