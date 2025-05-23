import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn ngôn ngữ lập trình yêu thích")

# Biến lưu giá trị được chọn
v = tk.IntVar()
v.set(1)  # mặc định chọn mục đầu tiên

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị giá trị được chọn
def ShowChoice():
    print("Bạn đã chọn:", v.get())

# Label hướng dẫn
tk.Label(root,
         text="Chọn ngôn ngữ lập trình bạn thích:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các radio button
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

# Vòng lặp sự kiện chính
root.mainloop()