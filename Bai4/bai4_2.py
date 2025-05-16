print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
S = input('Nhập chuỗi: ')                   # Nhập một chuỗi từ bàn phím và gán cho biến S
for ch in S:                                # Duyệt từng ký tự trong chuỗi S
    if ch != ' ' and ch != '\t':            # Nếu ký tự không phải là dấu cách (' ') và không phải là tab ('\t')
        print(ch)                           # Thì in ra ký tự đó