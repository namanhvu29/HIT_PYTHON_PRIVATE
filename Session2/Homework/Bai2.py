print("Hay nhap vao mot chuoi ki tu: ")
string = str(input())

if "hit" or "HIT" in string:
    print(True)
else:
    print(False)
if "15" not in string:
    print(True)
else:
    print(False)