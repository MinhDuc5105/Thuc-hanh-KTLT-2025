print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def find_longest_words(filename):  # Định nghĩa hàm tìm các từ dài nhất trong tệp
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # Mở tệp ở chế độ đọc, mã hóa UTF-8
            words = f.read().split()  # Đọc toàn bộ nội dung, tách thành danh sách các từ (theo dấu cách)
            max_len = max(len(word) for word in words)  # Tìm chiều dài lớn nhất trong các từ
            longest_words = [word for word in words if len(word) == max_len]  # Lấy danh sách các từ có độ dài bằng max_len
            print("Từ dài nhất là:", longest_words)  # In danh sách từ dài nhất
    except FileNotFoundError:  # Nếu tệp không tồn tại
        print("Không tìm thấy tệp.")  # Thông báo lỗi

# Gọi hàm với tệp 'D:/pt/name.txt'
find_longest_words('D:/pt/name.txt')