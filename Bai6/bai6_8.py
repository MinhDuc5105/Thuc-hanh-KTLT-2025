print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


class Bank:  # Định nghĩa lớp Bank quản lý tài khoản ngân hàng

    Account_type = "Savings"  # Thuộc tính lớp, loại tài khoản chung mặc định
    location = "Guntur"       # Thuộc tính lớp, địa điểm chung mặc định

    def __init__(self, name, Account_Number, balance):  # Hàm khởi tạo đối tượng
        self.name = name                   # Tên chủ tài khoản
        self.Account_Number = Account_Number  # Số tài khoản
        self.balance = balance             # Số dư tài khoản
        self.Account_type = Bank.Account_type  # Gán thuộc tính tài khoản loại Savings (từ lớp)
        self.location = Bank.location          # Gán thuộc tính địa điểm (từ lớp)

    def __repr__(self):  # Hàm đặc biệt, trả về chuỗi đại diện cho đối tượng khi in ra
        print("Welcome to the SBI ATM Machine")  # In lời chào
        print("-----------------------------------")  # In dòng phân cách
        account_pin = int(input("Please enter your pin number: "))  # Nhập mã PIN từ người dùng
        if account_pin == 123:  # Nếu PIN đúng (123)
            self.Account()      # Gọi hàm Account để thao tác tài khoản
        else:                  # Nếu PIN sai
            print("Pin Incorrect. Please try again")  # In thông báo lỗi
            self.Error()        # Gọi hàm Error để nhập lại PIN
        return ' '.join([self.name, str(self.Account_Number)])  # Trả về chuỗi gồm tên + số tài khoản

    def Error(self):  # Hàm xử lý khi nhập PIN sai
        account_pin = int(input("Please enter your pin number again: "))  # Nhập lại PIN
        if account_pin == 123:  # Nếu đúng PIN
            self.Account()      # Gọi hàm Account
        else:                   # Nếu sai tiếp
            print("Pin Incorrect. Please try again")  # Thông báo lỗi
            self.Error()        # Đệ quy gọi lại chính hàm để nhập PIN tiếp

    def Account(self):  # Hàm chính xử lý các thao tác với tài khoản
        print("Your Card Number is: XXXX XXXX XXXX 1337")  # In số thẻ (cố định)
        print("Would you like to deposit / withdraw / check balance?")  # Gợi ý thao tác
        while True:  # Vòng lặp vô hạn cho đến khi người dùng chọn thoát
            print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")  # In menu thao tác
            option = int(input("Please enter your choice: "))  # Nhập lựa chọn người dùng
            if option == 1:  # Nếu chọn xem số dư
                self.Balance()  # Gọi hàm in số dư
            elif option == 2:  # Nếu chọn rút tiền
                self.Withdraw()  # Gọi hàm rút tiền
            elif option == 3:  # Nếu chọn gửi tiền
                self.Deposit()  # Gọi hàm gửi tiền
            elif option == 4:  # Nếu chọn thoát
                self.Exit()     # Gọi hàm thoát
                break          # Thoát vòng lặp
            else:  # Nếu chọn sai số
                print("Invalid option. Please try again.")  # Thông báo sai

    def Balance(self):  # Hàm in số dư hiện tại
        print("Balance:", self.balance)

    def Withdraw(self):  # Hàm xử lý rút tiền
        w = float(input("Please enter amount to withdraw: "))  # Nhập số tiền muốn rút
        if self.balance >= w and w > 0:  # Kiểm tra số dư đủ và số tiền hợp lệ (>0)
            self.balance -= w  # Trừ số tiền rút khỏi số dư
            print("Your transaction is successful.")
            print("Your Balance:", self.balance)  # In số dư sau rút
        else:  # Nếu không đủ tiền hoặc nhập không hợp lệ
            print("Transaction cancelled. Not enough balance.")

    def Deposit(self):  # Hàm xử lý gửi tiền
        d = float(input("Please enter amount to deposit: "))  # Nhập số tiền gửi
        if d > 0:  # Nếu số tiền hợp lệ (>0)
            self.balance += d  # Cộng tiền vào số dư
            print("Your transaction is successful.")
            print("Your Balance:", self.balance)  # In số dư sau gửi
        else:  # Nếu số tiền không hợp lệ
            print("Invalid amount.")

    def Exit(self):  # Hàm thoát chương trình
        print("Exit")
        print("Thank you for using our ATM!")

# Chạy chương trình
if __name__ == "__main__":
    t1 = Bank("Mahesh", 1453210145, 5000)  # Tạo đối tượng tài khoản ngân hàng mới
    print(t1)  # Khi in, tự động gọi __repr__, bắt đầu quá trình nhập PIN và thao tác ATM