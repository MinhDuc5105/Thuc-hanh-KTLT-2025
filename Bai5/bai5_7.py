print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import numpy as np  # Nhập thư viện NumPy

# Định nghĩa kiểu dữ liệu cho mảng: mỗi phần tử là một record gồm 3 trường:
data_type = [('name', 'S15'),  # Trường "name" có kiểu chuỗi byte dài tối đa 15 ký tự
             ('class', int),   # Trường "class" là số nguyên (lớp học)
             ('height', float)]# Trường "height" là số thực (chiều cao)

# Danh sách thông tin sinh viên: mỗi tuple tương ứng 1 sinh viên
students_details = [('James', 5, 48.5),
                    ('Nail', 6, 52.5),
                    ('Paul', 5, 42.10),
                    ('Pit', 5, 40.11)]

# Tạo mảng có cấu trúc (structured array) theo kiểu dữ liệu đã định nghĩa
students = np.array(students_details, dtype=data_type)

print("Original array:")  # In mảng gốc chưa sắp xếp
print(students)

print("Sort by height")  # In mảng sau khi sắp xếp theo trường 'height'
print(np.sort(students, order='height'))