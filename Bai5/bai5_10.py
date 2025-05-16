print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from bubble_sort_module import bubbleSort
# Nhập hàm bubbleSort từ file module tự tạo tên là bubble_sort_module.py

nlist = list(map(int, input("Nhập list số, cách nhau bởi dấu phẩy: ").split(',')))
# Nhập danh sách số từ người dùng, tách bằng dấu phẩy → ép thành int → đưa vào list

sorted_list = bubbleSort(nlist)
# Gọi hàm bubbleSort để sắp xếp danh sách

print("Sau khi sắp xếp:", sorted_list)
# In danh sách đã sắp xếp