print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import numpy as np  # Nhập thư viện NumPy

# Tạo mảng ID sinh viên
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])

# Tạo mảng chiều cao tương ứng với từng sinh viên
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sắp xếp ưu tiên theo height, nếu height trùng thì sắp tiếp theo id
indices = np.lexsort((student_id, student_height))
# Trong np.lexsort, thứ tự ưu tiên sắp xếp là: ưu tiên cuối cùng truyền vào xếp trước
# → height được xếp **trước**, id được dùng để **phân loại khi height bằng nhau**

print("Chỉ số:")
print(indices)  # In ra chỉ số của các phần tử sau khi sắp xếp

print("Dữ liệu sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])  # In từng cặp ID và chiều cao theo thứ tự đã sắp