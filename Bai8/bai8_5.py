print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import tkinter as tk
# Nhập thư viện tkinter, đặt bí danh là tk.

root = tk.Tk()
# Tạo cửa sổ chính.

root.title("Radio Button Example")
# Đặt tiêu đề cửa sổ.

v = tk.IntVar()
v.set(1)
# Tạo biến kiểu IntVar dùng lưu giá trị lựa chọn của radio button.
# Khởi tạo giá trị mặc định là 1 (tương ứng "Python").

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]
# Danh sách các lựa chọn ngôn ngữ lập trình kèm giá trị số.

def ShowChoice():
    print("Bạn đã chọn:", v.get())
# Hàm xử lý khi người dùng chọn radio button.
# In ra giá trị hiện tại của biến v.

tk.Label(
    root,
    text="Choose your favourite programming language:",
    justify=tk.LEFT,
    padx=20
).pack()
# Tạo nhãn tiêu đề trong cửa sổ, căn trái, cách lề trái 20 pixel.

for lang, val in languages:
    tk.Radiobutton(
        root,
        text=lang,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val
    ).pack(anchor=tk.W)
# Vẽ các radio button theo từng ngôn ngữ trong danh sách.
# - text: tên ngôn ngữ hiển thị.
# - padx=20: khoảng cách padding ngang trong button.
# - variable=v: tất cả radio button này cùng dùng biến v để lưu lựa chọn.
# - command=ShowChoice: khi chọn sẽ gọi hàm ShowChoice.
# - value=val: giá trị của radio button đó.
# - pack(anchor=tk.W): căn về phía bên trái (West).

root.mainloop()
# Bắt đầu vòng lặp chính để chạy giao diện.