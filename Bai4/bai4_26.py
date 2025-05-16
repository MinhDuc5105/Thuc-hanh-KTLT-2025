print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
so_du = 0                                  # Khởi tạo số dư tài khoản ban đầu là 0

while True:                                # Vòng lặp vô hạn, sẽ kết thúc khi người dùng nhập dòng trống
    try:
        s = input()                        # Nhập một dòng lệnh từ bàn phím (ví dụ: D 100 hoặc W 50)

        if not s:                          # Nếu dòng trống → kết thúc vòng lặp
            break

        action, amount = s.split()         # Tách chuỗi thành 2 phần: hành động ('D' hoặc 'W') và số tiền

        amount = int(amount)               # Chuyển phần số tiền sang kiểu số nguyên

        if action == 'D':                  # Nếu hành động là 'D' (Deposit - gửi tiền)
            so_du += amount                # Cộng tiền vào số dư

        elif action == 'W':                # Nếu hành động là 'W' (Withdraw - rút tiền)
            so_du -= amount                # Trừ tiền khỏi số dư
    except:                                # Nếu có lỗi xảy ra (ví dụ: nhập sai định dạng)
        break                              # Kết thúc vòng lặp


print("Số dư tài khoản:", so_du)           # In ra số dư cuối cùng của tài khoản
