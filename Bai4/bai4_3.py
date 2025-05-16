print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
S = input('Nhập chuỗi: ')                         # Nhập một chuỗi từ bàn phím và lưu vào biến S
for ch in S:                                      # Lặp qua từng ký tự trong chuỗi S
    if ch != ' ' and ch != '\t':                  # Nếu ký tự không phải khoảng trắng (' ') và không phải tab ('\t')
        print(ch.upper())                         # In ký tự đó dưới dạng in hoa (chữ hoa)