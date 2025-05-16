print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
#a
from tkinter import *


root = Tk()
# Tạo cửa sổ chính của ứng dụng.

root.title("Thông tin cá nhân")
# Đặt tiêu đề cửa sổ thành "Thông tin cá nhân".

root.geometry("300x200")
# Đặt kích thước cửa sổ là 300 pixel rộng, 200 pixel cao.

Label(root, text="Họ tên: Nguyễn Văn A", font=("Arial", 12)).pack(pady=5)
# Tạo nhãn hiển thị chữ "Họ tên: Nguyễn Văn A", font Arial cỡ 12,
# đặt cách trên dưới 5 pixel để tạo khoảng cách.

Label(root, text="Ngày sinh: 01/01/2000", font=("Arial", 12)).pack(pady=5)
# Tạo nhãn hiển thị "Ngày sinh: 01/01/2000" với font và khoảng cách tương tự.

Label(root, text="MSSV: 123456789", font=("Arial", 12)).pack(pady=5)
# Tạo nhãn hiển thị "MSSV: 123456789".

Label(root, text="Ngành học: Công nghệ thông tin", font=("Arial", 12)).pack(pady=5)
# Tạo nhãn hiển thị "Ngành học: Công nghệ thông tin".

root.mainloop()
# Bắt đầu vòng lặp sự kiện của GUI, giữ cửa sổ hiển thị và chờ tương tác.
#b
from tkinter import *
from tkinter import messagebox
# Nhập thư viện tkinter và messagebox để dùng hộp thoại thông báo.

def show_selection():
    choice = var.get()
    messagebox.showinfo("Lựa chọn", f"Bạn đã chọn: {choice}")
# Hàm hiển thị hộp thoại thông báo khi người dùng nhấn nút,
# lấy giá trị hiện tại của biến var (giá trị radio button được chọn).

root = Tk()
# Tạo cửa sổ chính.

root.title("Welcome")
# Đặt tiêu đề cửa sổ thành "Welcome".

root.geometry("300x100")
# Đặt kích thước cửa sổ 300x100 pixel.

var = IntVar()
var.set(1)  # thiết lập mặc định là First
# Tạo biến kiểu IntVar để lưu lựa chọn của nhóm radio button,
# khởi tạo giá trị mặc định là 1 (radio button "First" được chọn).

Radiobutton(root, text="First", variable=var, value=1).pack(side=LEFT)
Radiobutton(root, text="Second", variable=var, value=2).pack(side=LEFT)
Radiobutton(root, text="Third", variable=var, value=3).pack(side=LEFT)
# Tạo 3 radio button với nhãn "First", "Second", "Third",
# liên kết chung biến var để quản lý lựa chọn,
# giá trị tương ứng là 1, 2, 3,
# và đặt theo chiều ngang từ trái sang phải (side=LEFT).

Button(root, text="Click Me", command=show_selection).pack(side=LEFT)
# Tạo nút "Click Me", khi nhấn sẽ gọi hàm show_selection,
# nút đặt bên cạnh các radio button theo chiều ngang.

root.mainloop()
# Bắt đầu vòng lặp sự kiện GUI.