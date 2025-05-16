def square(n):            # Định nghĩa hàm square nhận 1 tham số n
    return n * n          # Trả về bình phương của n (n nhân n)

def cube(n):              # Định nghĩa hàm cube nhận 1 tham số n
    return n * n * n      # Trả về lập phương của n (n nhân n nhân n)

def average(values):                  # Định nghĩa hàm average nhận 1 danh sách values
    nvals = len(values)               # Lưu số lượng phần tử trong danh sách vào biến nvals
    sum = 0.0                         # Tạo biến sum (kiểu float) để tính tổng
    for v in values:                  # Duyệt qua từng phần tử v trong danh sách
        sum += v                      # Cộng giá trị v vào biến sum
    return float(sum) / nvals         # Tính trung bình = tổng chia số phần tử, ép kiểu float để chắc chắn