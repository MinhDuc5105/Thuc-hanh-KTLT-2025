print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
result = []
# Khởi tạo danh sách rỗng để lưu các số thỏa điều kiện
for num in range(1000, 3001):
# Duyệt qua tất cả các số nguyên từ 1000 đến 3000 (bao gồm 1000, không bao gồm 3001)
    s = str(num)
# Chuyển số hiện tại sang chuỗi để dễ duyệt từng chữ số
    if all(int(ch) % 2 == 0 for ch in s):
    # Kiểm tra nếu **tất cả các chữ số** đều là số chẵn (0, 2, 4, 6, 8)
        result.append(s)
    # Nếu đúng, thêm chuỗi số đó vào danh sách kết quả

print(','.join(result))
# In ra các số thỏa điều kiện, cách nhau bằng dấu phẩy