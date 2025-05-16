print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from mymodule5_5 import find_max, sort_list
# Nhập 2 hàm `find_max` và `sort_list` từ module tự tạo tên là mymodule5_5.py

n = int(input("Nhập số lượng phần tử trong danh sách: "))
# Nhập số lượng phần tử người dùng muốn thêm, chuyển thành kiểu int

lst = []  # Tạo danh sách rỗng để chứa các phần tử

for i in range(n):
    num = float(input(f"Nhập phần tử thứ {i + 1}: "))  # Nhập từng phần tử, chuyển thành float
    lst.append(num)  # Thêm phần tử vào danh sách

sorted_list = sort_list(lst)  # Gọi hàm sắp xếp danh sách (trả về danh sách mới đã sắp xếp tăng dần)
maximum = find_max(lst)       # Gọi hàm tìm phần tử lớn nhất (do bạn định nghĩa trong module)
minimum = min(lst)            # Dùng hàm có sẵn của Python để tìm phần tử nhỏ nhất

index_max = lst.index(maximum)  # Tìm vị trí (chỉ số) của phần tử lớn nhất trong danh sách gốc
index_min = lst.index(minimum)  # Tìm vị trí của phần tử nhỏ nhất

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_list)
# In danh sách đã sắp xếp theo thứ tự tăng dần

print("Phần tử lớn nhất:", maximum, "ở vị trí:", index_max)
# In phần tử lớn nhất và vị trí của nó trong danh sách ban đầu

print("Phần tử nhỏ nhất:", minimum, "ở vị trí:", index_min)
# In phần tử nhỏ nhất và vị trí của nó trong danh sách ban đầu