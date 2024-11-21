dict1 = {}
n = int(input("Nhap so phan tu trong dict: "))
for _ in range(n):
    key = input("Nhap key: ")
    value = input("Nhap value: ")
    dict1[key] = value

values = list(dict1.values())
if len(values) != len(set(values)):
    print("None")
else:
    dict_new = {v: k for k, v in dict1.items()}
    print("Dict moi sau khi hoan doi:", dict_new)
