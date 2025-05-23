import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn ngôn ngữ lập trình yêu thích")

# Biến lưu lựa chọn
v = tk.IntVar()
v.set(1)  # mặc định là Python

# Danh sách ngôn ngữ lập trình
languages = [
    ("Python 1", 1),
    ("Perl 2", 2),
    ("Java 3", 3),
    ("C++ 4", 4),
    ("C 5", 5)
]

# Hàm hiển thị giá trị đã chọn
def ShowChoice():
    print("Bạn đã chọn:", v.get())

# Label hướng dẫn
tk.Label(root,
         text="Choose your favourite\nprogramming language:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các nút Radio kiểu button (không có chấm tròn)
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,
                   padx=20,
                   variable=v,
                   value=val,
                   command=ShowChoice,
                   indicatoron=0,  # ✅ đây là phần quan trọng để chuyển sang dạng nút
                   width=20,
                   relief="raised").pack(anchor=tk.W)

# Chạy vòng lặp giao diện
root.mainloop()