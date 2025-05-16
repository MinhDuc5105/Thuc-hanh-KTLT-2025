print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
S = input('Nhập chuỗi: ')                            # Nhập một chuỗi từ bàn phím và gán vào biến S
for ch in S:                                         # Lặp qua từng ký tự trong chuỗi S
    if ch not in '0,1,2,3,4,5,6,7,8,9':              # Nếu ký tự không phải là số từ 0 đến 9
        print(ch)                                    # In ký tự đó ra màn hình