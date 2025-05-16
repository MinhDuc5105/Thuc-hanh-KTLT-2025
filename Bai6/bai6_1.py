print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class Circle(object):  # Khai báo lớp (class) có tên là Circle, kế thừa từ object
    def __init__(self, r):  # Hàm khởi tạo (constructor), chạy khi tạo đối tượng Circle
        self.radius = r  # Gán giá trị bán kính r cho thuộc tính radius của đối tượng

    def area(self):  # Định nghĩa phương thức area để tính diện tích hình tròn
        return self.radius ** 2 * 3.14  # Trả về diện tích theo công thức πr² (dùng 3.14 thay cho π)

aCircle = Circle(2)  # Tạo một đối tượng Circle với bán kính = 2 và gán vào biến aCircle
print(aCircle.area())  # Gọi phương thức area() để tính và in diện tích hình tròn (kết quả: 12.56)