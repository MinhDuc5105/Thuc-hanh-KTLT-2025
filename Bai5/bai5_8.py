print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from sequential_search_module import Sequential_Search
# Nhập hàm `Sequential_Search` từ file module cùng thư mục tên là sequential_search_module.py

# Nhập danh sách số nguyên từ người dùng, cách nhau bởi dấu phẩy
dlist = list(map(int, input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ").split(',')))

item = int(input("Nhập số cần tìm: "))  # Nhập số cần tìm (kiểu int)

# Gọi hàm tìm kiếm tuần tự
found, position = Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Tìm thấy {item} tại vị trí {position}")  # Nếu tìm thấy, in vị trí
else:
    print(f"Không tìm thấy {item}")  # Nếu không tìm thấy