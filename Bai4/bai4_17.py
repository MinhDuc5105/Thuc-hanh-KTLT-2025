print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def tong_uoc_thuc_su(x):           # Định nghĩa hàm tính tổng các ước thực sự của x (không bao gồm chính nó)
    tong = 0                       # Khởi tạo biến tổng = 0
    for i in range(1, x):          # Duyệt từ 1 đến x - 1
        if x % i == 0:             # Nếu i là ước của x
            tong += i              # Cộng i vào biến tổng
    return tong                    # Trả về tổng các ước thực sự
n = int(input("Nhập n: "))         # Nhập số nguyên n từ bàn phím

print(f"Các số nhỏ hơn {n} có tổng ước thực sự lớn hơn chính nó:")
# In thông báo: liệt kê các số nhỏ hơn n mà tổng ước thực sự của chúng lớn hơn chính nó
for i in range(1, n):              # Duyệt qua tất cả các số từ 1 đến n - 1
    if tong_uoc_thuc_su(i) > i:    # Nếu tổng ước thực sự của i > i (nghĩa là số "giàu ước")
        print(i, end=' ')          # In ra số đó, cách nhau bằng dấu cách