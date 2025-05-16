print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = input('Nhập chuỗi: ').split()     # Nhập một chuỗi và tách thành danh sách các từ (cắt theo khoảng trắng)
x = ds[1:-1]                            # Lấy các phần tử từ vị trí thứ 1 đến trước phần tử cuối (bỏ phần tử đầu và cuối)
for c in x:                             # Duyệt qua từng phần tử trong danh sách x
    print(c)                            # In từng phần tử trên một dòng riêng