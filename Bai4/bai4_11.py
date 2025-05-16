print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = input('Nhập chuỗi: ').split()     # Nhập một chuỗi, tách thành danh sách các từ cách nhau bởi khoảng trắng
ds.append('abc')                       # Thêm chuỗi 'abc' vào cuối danh sách ds
for dh in ds:                          # Lặp qua từng phần tử trong danh sách ds
    print(dh)                          # In từng phần tử trên một dòng riêng