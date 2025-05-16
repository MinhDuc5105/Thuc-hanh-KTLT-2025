print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from tkinter import *
# Nhập tất cả các lớp, hàm từ thư viện tkinter để xây dựng GUI.

window = Tk()
# a) Tạo cửa sổ chính của ứng dụng, đặt tên biến là window.

window.title("Welcome to LikeGeeks app")
# Đặt tiêu đề cho cửa sổ là "Welcome to LikeGeeks app".

window.geometry('350x200')
# Đặt kích thước cửa sổ là 350 pixel rộng, 200 pixel cao.

lbl = Label(window, text="Hello")
# b) Tạo một nhãn (Label) bên trong cửa sổ window, hiển thị chữ "Hello".

lbl.grid(column=0, row=0)
# Đặt vị trí nhãn lbl trên lưới (grid) ở cột 0, hàng 0.

def clicked():
    # c) Định nghĩa hàm xử lý sự kiện khi nút được bấm.
    lbl.configure(text="Button was clicked !!")
    # Thay đổi nội dung nhãn lbl thành "Button was clicked !!".

btn = Button(window,
             text="Click Me",
             command=clicked,
             bg="lightblue",      # màu nền nút là xanh nhạt
             fg="darkred")        # màu chữ trên nút là đỏ đậm
# b) Tạo nút (Button) trong cửa sổ window, với nhãn "Click Me",
# khi bấm sẽ gọi hàm clicked, có màu nền và màu chữ tùy chỉnh.

btn.grid(column=1, row=0)
# Đặt nút btn ở vị trí cột 1, hàng 0 trong lưới.

window.mainloop()
# d) Bắt đầu vòng lặp chính của GUI, để cửa sổ hiện ra và lắng nghe sự kiện.