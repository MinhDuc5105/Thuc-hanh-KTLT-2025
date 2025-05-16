print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def write_list_to_file(filename, data_list):  # Định nghĩa hàm ghi danh sách data_list vào tệp filename
    with open(filename, 'w', encoding='utf-8') as f:  # Mở tệp ở chế độ ghi (w), mã hóa UTF-8
        for item in data_list:  # Duyệt từng phần tử trong danh sách
            f.write(str(item) + '\n')  # Ghi phần tử (chuyển sang chuỗi) vào tệp, kết thúc bằng xuống dòng
    print("Đã ghi danh sách vào tệp.")  # Thông báo đã ghi thành công

# Ví dụ sử dụng
my_list = ['apple', 'banana', 'cherry']  # Danh sách mẫu
write_list_to_file('D:/pt/fruit.txt', my_list)  # Gọi hàm ghi danh sách vào tệp 'D:/pt/fruit.txt'