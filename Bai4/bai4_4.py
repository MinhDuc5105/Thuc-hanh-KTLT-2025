print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ds = input("Danh sách: ").split()     # Nhập một chuỗi, tách thành danh sách các từ bằng khoảng trắng và gán vào biến ds
print(ds)                              # In ra toàn bộ danh sách (list) vừa nhập
for so in ds:                          # Lặp qua từng phần tử (so) trong danh sách ds
    print(so)                          # In từng phần tử trên một dòng riêng