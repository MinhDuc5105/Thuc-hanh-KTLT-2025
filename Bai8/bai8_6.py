print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
from tkinter import *
from tkinter import messagebox
# Nhập tất cả các lớp từ tkinter và messagebox để hiện hộp thoại thông báo.

def NewFile():
    messagebox.showinfo("New File", "Bạn đã chọn: New File!")
# Hàm xử lý khi chọn menu File > New, hiển thị hộp thoại thông báo.

def OpenFile():
    messagebox.showinfo("Open File", "Bạn đã chọn: Open File!")
# Hàm xử lý khi chọn File > Open.

def ExitApp():
    root.quit()
# Hàm thoát ứng dụng.

def InsText():
    messagebox.showinfo("Insert Text", "Bạn đã chọn: Insert Text")
# Xử lý khi chọn Insert > Text.

def InsPic():
    messagebox.showinfo("Insert Picture", "Bạn đã chọn: Insert Picture")
# Xử lý khi chọn Insert > Picture.

def About():
    messagebox.showinfo("About", "Đây là ví dụ về menu trong tkinter")
# Xử lý khi chọn Help > About, hiển thị thông tin ứng dụng.

root = Tk()
# Tạo cửa sổ chính.

root.title("Menu Example")
# Đặt tiêu đề cửa sổ.

root.geometry("300x200")
# Đặt kích thước cửa sổ.

menu = Menu(root)
# Tạo thanh menu chính.

root.config(menu=menu)
# Cấu hình cửa sổ chính sử dụng menu vừa tạo.

filemenu = Menu(menu, tearoff=0)
# Tạo menu con File, tearoff=0 để không cho menu rời ra thành cửa sổ riêng.

menu.add_cascade(label="File", menu=filemenu)
# Thêm menu File vào thanh menu chính.

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitApp)
# Thêm các lệnh con vào menu File, phân cách bằng separator.

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)
# Tạo menu Insert và thêm các lệnh con.

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
# Tạo menu Help với lệnh About.

root.mainloop()
# Chạy vòng lặp chính, hiển thị cửa sổ và chờ sự kiện.