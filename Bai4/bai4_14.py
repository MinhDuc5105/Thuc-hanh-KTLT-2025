print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = '5 4 3 2 1'.split()    # Tách chuỗi thành danh sách: ['5', '4', '3', '2', '1'] (các phần tử là chuỗi)
ds.sort()                   # Sắp xếp danh sách theo thứ tự bảng chữ cái (vì các phần tử là chuỗi)
for ch in ds:               # Duyệt qua từng phần tử trong danh sách đã sắp xếp
    print(ch)               # In ra từng phần tử trên một dòng