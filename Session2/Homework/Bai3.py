string = "Chao mung den CLB Tin hoc HIT"
print(string)
string1 = "10 diem"
string2 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "
print( string2, string1)

for char in string2:
    if char.isupper():
        print(char, end=" ")
print("")
for char in string2:
    if char.islower():
        print(char, end=" ")
print("")

if "CNTT" in string2:
    print("Yes")
else:
    print("No")

for char in string2:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")