print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
S = input('Nhập chuỗi: ').split()            # Nhập chuỗi, tách thành danh sách các từ bằng khoảng trắng
kitudai = max(S, key=len)                    # Tìm từ dài nhất trong danh sách S, dựa trên độ dài (len)
print(kitudai)                               # In ra từ dài nhất