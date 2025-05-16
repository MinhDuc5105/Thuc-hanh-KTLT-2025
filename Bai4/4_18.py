print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
n = int(input("Nhập số nguyên n: "))       # Nhập số nguyên n từ bàn phím và chuyển thành kiểu int
fibo = []                                  # Tạo danh sách rỗng để chứa dãy Fibonacci

a, b = 0, 1                                 # Khởi tạo 2 số đầu tiên trong dãy Fibonacci: a = 0, b = 1
while a < n:                               # Lặp khi a còn nhỏ hơn n
    fibo.append(a)                         # Thêm số a vào danh sách fibo
    a, b = b, a + b                         # Cập nhật: a = b, b = a + b (chuyển sang số tiếp theo trong dãy)

print("Dãy Fibonacci nhỏ hơn", n, "là:")   # In thông báo
print(fibo)                                # In toàn bộ dãy Fibonacci vừa tạo