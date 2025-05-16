print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def copy_file(source, target):  # Định nghĩa hàm sao chép nội dung từ file nguồn sang file đích
    try:
        with open(source, 'r', encoding='utf-8') as src, open(target, 'w', encoding='utf-8') as dst:  # Mở file nguồn đọc, file đích ghi
            dst.write(src.read())  # Đọc toàn bộ nội dung file nguồn và ghi vào file đích
        print("Đã sao chép nội dung từ", source, "sang", target)  # In thông báo thành công
    except FileNotFoundError:  # Nếu file nguồn không tìm thấy
        print("Không tìm thấy tệp nguồn.")  # In thông báo lỗi

# Gọi hàm với file nguồn và file đích
copy_file('D:/pt/name.txt', 'D:/pt/name_copy.txt')