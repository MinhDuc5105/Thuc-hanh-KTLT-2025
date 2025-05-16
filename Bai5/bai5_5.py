print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from mymodule5_5 import find_max, sort_list
# Nhập hai hàm `find_max` và `sort_list` từ module tự tạo tên là `mymodule5_5.py`

n = int(input("Nhập số lượng phần tử trong danh sách: "))
# Yêu cầu người dùng nhập số lượng phần tử, chuyển sang kiểu int

lst = []  # Tạo danh sách rỗng
for i in range(n):
    num = float(input(f"Nhập phần tử thứ {i + 1}: "))  # Nhập từng số, chuyển sang float
    lst.append(num)  # Thêm số vào danh sách

sorted_list = sort_list(lst)  # Gọi hàm `sort_list` từ module để sắp xếp danh sách
maximum = find_max(lst)       # Gọi hàm `find_max` để tìm phần tử lớn nhất
minimum = min(lst)            # Dùng hàm `min()` có sẵn của Python để tìm phần tử nhỏ nhất

print("Danh sách sau khi sắp xếp:", sorted_list)  # In danh sách đã sắp xếp
print("Phần tử lớn nhất:", maximum)               # In phần tử lớn nhất
print("Phần tử nhỏ nhất:", minimum)               # In phần tử nhỏ nhất
