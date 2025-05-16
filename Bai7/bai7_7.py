print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def count_lines(filename):  # Định nghĩa hàm đếm số dòng trong tệp với tên tệp truyền vào
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # Mở tệp ở chế độ đọc, mã hóa UTF-8
            lines = f.readlines()  # Đọc tất cả các dòng trong tệp vào danh sách lines
            print("Số dòng trong tệp là:", len(lines))  # In ra số lượng dòng (độ dài danh sách lines)
    except FileNotFoundError:  # Xử lý ngoại lệ nếu tệp không tồn tại
        print("Không tìm thấy tệp.")  # In thông báo lỗi

# Gọi hàm với tệp 'D:/pt/name.txt'
count_lines('D:/pt/name.txt')