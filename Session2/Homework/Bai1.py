from six import binary_type

print("So a = 5")
print("So b = 6")
a, b = 5, 6
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a x b = ", a * b)
print("a // b = ", a // b)
print("a ^ b = ", a ** b)
print("a % b = ", a % b)
print("So lon nhat giua a va b la ", max(a,b))
print("a AND b ", a & b)
print("a OR b ", a | b)
print("a XOR b ", a ^ b)
print("NOT a == b", not(a==b))
print("a dich phai 5 bit", a >> 5)
print("a dich trai 5 bit ", a << 5)
binary_a = bin(a)[2:]
reverse_a = binary_a[::-1]
print("He co so 2 dao nguoc cua a la ", reverse_a)


