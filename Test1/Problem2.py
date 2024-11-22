def dem_chu_cai(tu):
    ket_qua = {}
    for chu in tu.lower():
        if chu.isalpha():
            ket_qua[chu] = ket_qua.get(chu, 0) + 1
    return ket_qua
    
tu = input("nhap tu: ")
ket_qua = dem_chu_cai(tu)
print("so lan xuat hien:" , ket_qua)