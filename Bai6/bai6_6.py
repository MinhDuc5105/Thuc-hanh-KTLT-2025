print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class StringHandler:  # Định nghĩa lớp StringHandler để quản lý chuỗi
    def __init__(self):  # Hàm khởi tạo, gọi khi tạo đối tượng mới
        self.s = ""  # Khởi tạo thuộc tính s là chuỗi rỗng

    def get_String(self):  # Phương thức nhập chuỗi từ người dùng
        self.s = input("Nhập chuỗi: ")  # Gán chuỗi nhập được vào thuộc tính s

    def print_String(self):  # Phương thức in chuỗi đã lưu
        print(self.s.upper())  # In chuỗi s dưới dạng chữ hoa

# Ví dụ sử dụng
handler = StringHandler()  # Tạo đối tượng handler từ lớp StringHandler
handler.get_String()  # Gọi phương thức để nhập chuỗi
handler.print_String()  # Gọi phương thức để in chuỗi chữ hoa