print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = input("Nhập số nhị phân cách nhau bằng 1 dấu phẩy: ").split(',')
# Nhập chuỗi các số nhị phân cách nhau bằng dấu phẩy, rồi tách chúng thành danh sách

ds.sort()
# Sắp xếp danh sách theo thứ tự bảng chữ cái (tức là theo dạng chuỗi)

for ch in ds:
    print(ch)
# In từng số nhị phân đã sắp xếp trên một dòng riêng