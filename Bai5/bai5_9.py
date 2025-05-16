print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from binary_search_module import binary_search
# Nhập hàm binary_search từ module tự tạo tên là binary_search_module.py

lst = sorted(list(map(int, input("Nhập list số, cách nhau bởi dấu phẩy: ").split(','))))
# Nhập danh sách số nguyên cách nhau bởi dấu phẩy → ép kiểu int → sắp xếp tăng dần

val = int(input("Nhập giá trị cần tìm: "))
# Nhập giá trị cần tìm, ép sang int

print("Tìm thấy?" , binary_search(lst, val))
# Gọi hàm tìm nhị phân và in kết quả: True nếu tìm thấy, False nếu không