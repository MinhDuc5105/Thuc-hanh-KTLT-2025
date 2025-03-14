print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
name= input("Nhập trên người dùng: ")
password = input("Nhập mật khẩu: ").split(',')
import re
valid_password = []
def is_valid_password(key):
    if len(key) < 6 or len(key) > 12 :
        return False
    if not re.search("[a-z]", key):
        return False
    if not re.search("[0-9]", key):
        return False
    if not re.search("[A-Z]", key):
        return False
    if not re.search("[$ # @]", key):
        return False
    return True
for pwd in password:
    if is_valid_password(pwd):
        valid_password.append(pwd)
print(",".join(valid_password))



