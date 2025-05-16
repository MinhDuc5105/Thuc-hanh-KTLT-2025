print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
input_str = input("Nhập chuỗi nhị phân, cách nhau bởi dấu phẩy: ")
# Nhập một chuỗi gồm các số nhị phân, cách nhau bằng dấu phẩy (ví dụ: 1010,1111,10000)

items = input_str.split(',')
# Tách chuỗi thành danh sách các số nhị phân riêng lẻ

result = [x for x in items if int(x, 2) % 5 == 0]
# Duyệt từng phần tử x trong danh sách:
# - Chuyển x từ nhị phân sang thập phân bằng int(x, 2)
# - Kiểm tra nếu chia hết cho 5 → thêm x vào danh sách kết quả

print(','.join(result))
# In ra các số nhị phân chia hết cho 5, nối lại bằng dấu phẩy
