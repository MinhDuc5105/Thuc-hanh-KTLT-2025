print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class Nguoi(object):  # Định nghĩa lớp cha tên là Nguoi (Người), kế thừa từ object
    def getGender(self):  # Định nghĩa phương thức getGender
        return "Unknown"  # Mặc định trả về "Unknown" nếu chưa xác định giới tính

class Nam(Nguoi):  # Định nghĩa lớp Nam kế thừa từ lớp Nguoi
    def getGender(self):  # Ghi đè (override) phương thức getGender của lớp cha
        return "Nam"  # Trả về "Nam" nếu gọi từ đối tượng thuộc lớp Nam

class Nu(Nguoi):  # Định nghĩa lớp Nu kế thừa từ lớp Nguoi
    def getGender(self):  # Ghi đè phương thức getGender
        return "Nữ"  # Trả về "Nữ" nếu gọi từ đối tượng thuộc lớp Nu

aNam = Nam()  # Tạo đối tượng aNam từ lớp Nam
aNu = Nu()    # Tạo đối tượng aNu từ lớp Nu

print(aNam.getGender())  # Gọi phương thức getGender từ aNam → In ra "Nam"
print(aNu.getGender())   # Gọi phương thức getGender từ aNu → In ra "Nữ"