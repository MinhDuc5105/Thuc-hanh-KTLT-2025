print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class Hinhchunhat:  # Khai báo lớp Hinhchunhat (hình chữ nhật)
    def __init__(self, chieu_dai, chieu_rong):  # Hàm khởi tạo với 2 tham số: chiều dài và chiều rộng
        self.chieu_dai = chieu_dai  # Gán giá trị chiều dài cho thuộc tính chieu_dai của đối tượng
        self.chieu_rong = chieu_rong  # Gán giá trị chiều rộng cho thuộc tính chieu_rong của đối tượng

    def dientich(self):  # Định nghĩa phương thức dientich để tính diện tích
        return self.chieu_dai * self.chieu_rong  # Trả về tích của chiều dài và chiều rộng (diện tích)

# Ví dụ sử dụng:
hcn = Hinhchunhat(5, 3)  # Tạo đối tượng hình chữ nhật với chiều dài = 5, chiều rộng = 3
print("Diện tích hình chữ nhật là:", hcn.dientich())  # Gọi phương thức dientich và in kết quả