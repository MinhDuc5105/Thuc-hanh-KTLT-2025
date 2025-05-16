print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = 'chào buổi sáng 123'.split()     # Tách chuỗi thành danh sách các từ: ['chào', 'buổi', 'sáng', '123']
ds.remove('123')                      # Xóa phần tử '123' khỏi danh sách
for dh in ds:                         # Duyệt qua từng phần tử còn lại trong danh sách
    print(dh)                         # In ra từng phần tử trên một dòng riêng