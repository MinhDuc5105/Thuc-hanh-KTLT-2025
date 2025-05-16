print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import mymath5_1  # Nhập module mymath5_1 để sử dụng các hàm đã định nghĩa bên trong (square, cube, average)

values = [2, 4, 6, 8, 10]  # Tạo một danh sách các số nguyên

print('Squares:')  # In ra tiêu đề "Squares:"
for v in values:
    print(mymath5_1.square(v))  # In bình phương của từng giá trị trong danh sách (dùng hàm square từ module)

print('Cubes:')  # In ra tiêu đề "Cubes:"
for v in values:
    print(mymath5_1.cube(v))  # In lập phương của từng giá trị trong danh sách (dùng hàm cube từ module)

print('Average: ' + str(mymath5_1.average(values)))
# Tính trung bình các giá trị trong danh sách và in ra (ép kiểu float về chuỗi để nối)

import mymath5_1 as mt  # Nhập lại module với tên rút gọn là mt để tiện sử dụng sau này

print(mt.square(2))  # In bình phương của 2 (sử dụng module với tên rút gọn mt)
print(mt.square(3))  # In bình phương của 3 (sử dụng module với tên rút gọn mt)