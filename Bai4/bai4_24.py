print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
s = input("Nhập câu: ")                             # Nhập một chuỗi từ bàn phím và lưu vào biến s

chu_hoa = sum(c.isupper() for c in s)              # Đếm số chữ cái in hoa trong chuỗi s
chu_thuong = sum(c.islower() for c in s)           # Đếm số chữ cái thường trong chuỗi s

print("Chữ hoa:", chu_hoa)                         # In ra số lượng chữ in hoa
print("Chữ thường:", chu_thuong)                   # In ra số lượng chữ thường