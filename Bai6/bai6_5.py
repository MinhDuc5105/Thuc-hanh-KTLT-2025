print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class WordReverser:  # Định nghĩa lớp WordReverser để xử lý đảo ngược các từ trong câu
    def reverse_words(self, sentence):  # Phương thức để đảo ngược thứ tự từ trong câu
        words = sentence.split()  # Tách câu thành danh sách các từ, phân tách bởi khoảng trắng
        reversed_words = ' '.join(reversed(words))  # Đảo ngược danh sách từ và nối lại thành chuỗi
        return reversed_words  # Trả về câu đã được đảo thứ tự từ

# Ví dụ sử dụng
reverser = WordReverser()  # Tạo đối tượng từ lớp WordReverser
input_str = "hello .py"  # Chuỗi đầu vào
print(reverser.reverse_words(input_str))  # Gọi phương thức và in ra: ".py hello"