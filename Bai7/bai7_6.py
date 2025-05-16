print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import sys  # Thư viện hệ thống (ở đây chưa dùng đến)
import os   # Thư viện tương tác với hệ điều hành, dùng để lấy thông tin file

def file_read_from_tail(fname, lines):  # Hàm đọc file từ cuối, lấy ra số dòng 'lines' cuối
    bufsize = 8192  # Kích thước buffer đọc mỗi lần (8KB)
    fsize = os.stat(fname).st_size  # Lấy kích thước (byte) của file fname
    iter = 0  # Biến đếm số lần đọc từ cuối file
    data = []  # Danh sách chứa các dòng đọc được

    with open(fname, 'r', encoding='utf-8') as f:  # Mở file đọc (chế độ text, mã hóa UTF-8)
        while True:  # Vòng lặp đọc lặp lại đến khi đủ dòng hoặc đọc hết file
            iter += 1  # Tăng số lần đọc lên 1
            seek_pos = fsize - bufsize * iter  # Tính vị trí bắt đầu đọc: từ cuối file lùi lại bufsize * iter byte
            if seek_pos < 0:  # Nếu vị trí âm (quá đầu file)
                f.seek(0)     # Đặt con trỏ file về đầu file
            else:
                f.seek(seek_pos)  # Ngược lại, đặt con trỏ file tại vị trí tính được

            data = f.readlines()  # Đọc tất cả dòng từ vị trí con trỏ đến cuối file, lưu vào data

            # Nếu số dòng đọc được >= số dòng cần lấy hoặc đã đọc từ đầu file
            if len(data) >= lines or seek_pos <= 0:
                print(''.join(data[-lines:]))  # In ra dòng cuối (lines) dòng của data
                break  # Dừng vòng lặp

# Gọi hàm để đọc 2 dòng cuối file 'D:/pt/name.txt'
file_read_from_tail('D:/pt/name.txt', 2)