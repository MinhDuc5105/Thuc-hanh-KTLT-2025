print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
s = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")         # Nhập chuỗi chứa các số, cách nhau bởi dấu phẩy (ví dụ: 1,2,3,4)

numbers = list(map(int, s.split(',')))                      # Tách chuỗi theo dấu phẩy → danh sách chuỗi → chuyển từng phần tử thành số nguyên

le = [str(x) for x in numbers if x % 2 != 0]                # Duyệt từng số trong numbers, nếu là số lẻ (chia 2 dư 1) thì chuyển thành chuỗi và thêm vào danh sách mới

print(','.join(le))                                         # Nối các số lẻ (ở dạng chuỗi) bằng dấu phẩy và in ra