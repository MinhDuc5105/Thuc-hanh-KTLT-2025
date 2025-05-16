print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
s = input("Nhập câu: ")                          # Nhập một chuỗi (câu) từ bàn phím và gán vào biến s

chu_cai = sum(c.isalpha() for c in s)            # Đếm số chữ cái: duyệt từng ký tự c trong chuỗi s, nếu là chữ cái thì tính vào tổng
chu_so = sum(c.isdigit() for c in s)             # Đếm số chữ số: duyệt từng ký tự c trong chuỗi s, nếu là chữ số thì tính vào tổng

print("Số chữ cái là:", chu_cai)                 # In ra tổng số chữ cái
print("Số chữ số là:", chu_so)                   # In ra tổng số chữ số