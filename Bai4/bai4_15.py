print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = input("Nhập các từ tiếng Anh, cách nhau bằng dấu cách: ").split()
# Nhập chuỗi từ bàn phím, tách thành danh sách các từ theo dấu cách

ds.sort()
# Sắp xếp danh sách các từ theo thứ tự bảng chữ cái (tăng dần, từ A đến Z)

for ch in ds:
    print(ch)
# In từng từ đã sắp xếp trên một dòng riêng