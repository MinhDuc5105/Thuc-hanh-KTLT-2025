print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class RomanConverter:  # Định nghĩa lớp RomanConverter để chuyển đổi số La Mã sang số nguyên
    def __init__(self):  # Hàm khởi tạo, chạy khi tạo đối tượng
        self.roman_map = {  # Tạo từ điển ánh xạ các chữ số La Mã sang giá trị thập phân
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_int(self, s):  # Phương thức chuyển xâu La Mã s sang số nguyên
        total = 0      # Tổng kết quả
        prev = 0       # Biến lưu giá trị chữ số La Mã trước đó (dùng để so sánh)
        for char in reversed(s):  # Duyệt từng ký tự trong xâu từ phải sang trái
            curr = self.roman_map[char]  # Lấy giá trị tương ứng của ký tự
            if curr < prev:  # Nếu số hiện tại nhỏ hơn số trước đó → dạng trừ (như IV = 5 - 1)
                total -= curr  # Trừ đi giá trị hiện tại
            else:  # Ngược lại, cộng bình thường
                total += curr
                prev = curr  # Cập nhật giá trị trước đó
        return total  # Trả về kết quả cuối cùng

# Ví dụ sử dụng
converter = RomanConverter()  # Tạo đối tượng chuyển đổi
print(converter.roman_to_int("IX"))     # IX = 10 - 1 = 9
print(converter.roman_to_int("MCMXC"))  # MCMXC = 1000 + (1000-100) + (100 - 10) = 1990