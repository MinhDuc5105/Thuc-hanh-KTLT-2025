print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
try:
    with open(r'D:\pt\name.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("Nội dung tệp:")
        print(content)
except FileNotFoundError:
    print("Tệp không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
except Exception as e:
    print("Đã xảy ra lỗi:", e)