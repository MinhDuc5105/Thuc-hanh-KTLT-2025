print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
ho_ten = input("Nhập họ và tên riêng: ")    # Nhập vào một chuỗi chứa họ và tên riêng (2 từ), lưu vào biến ho_ten
ds = ho_ten.split()                         # Tách chuỗi thành danh sách các từ bằng khoảng trắng, lưu vào ds
ho = ds[0]                                  # Lấy phần tử đầu tiên (họ) từ danh sách
ten = ds[1]                                 # Lấy phần tử thứ hai (tên riêng) từ danh sách
print("Họ:", ho)                            # In ra phần họ
print("Tên riêng:", ten)                   # In ra phần tên riêng