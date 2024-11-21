
dangky = set(input("Nhap ten cac ban dang ky tham gia: ").split())
checked_in = set(input("Nhap ten cac ban da check in: ").split())


not_checked_in = dangky - checked_in
print(f"Cac ban chua check in: {not_checked_in}")


total = len(dangky.union(checked_in))
print(f"Tong so cac ban da dang ky va check in: {total}")


sap_xep_dangky = sorted(dangky)
print(f"Danh sach cac ban dang ky: {sap_xep_dangky}")
