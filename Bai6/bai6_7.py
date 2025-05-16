print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Ví dụ sử dụng
hinhtron = Circle(5)
print("Diện tích:", hinhtron.area())        # 78.5
print("Chu vi:", hinhtron.perimeter())      # 31.4