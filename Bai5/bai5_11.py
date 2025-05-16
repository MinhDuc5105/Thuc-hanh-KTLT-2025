print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import numpy as np  # Nhập thư viện NumPy

# Tạo mảng có cấu trúc (structured array), mỗi phần tử gồm 3 trường: name, class, height
data = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=[('name', 'U10'),   # U10: chuỗi Unicode tối đa 10 ký tự
          ('class', 'i4'),   # i4: số nguyên 4 byte
          ('height', 'f4')]) # f4: số thực 4 byte

# Sắp xếp theo 'class' trước, nếu trùng thì tiếp tục sắp theo 'height'
sorted_data = np.sort(data, order=['class', 'height'])

print(sorted_data)  # In kết quả sau khi sắp xếp