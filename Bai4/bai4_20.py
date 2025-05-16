print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def pascal_triangle(n):                # Định nghĩa hàm tạo tam giác Pascal với n dòng
    triangle = []                      # Khởi tạo danh sách rỗng để chứa các dòng của tam giác

    for i in range(n):                 # Lặp n lần để tạo từng dòng từ 0 đến n - 1
        row = [1]                      # Dòng nào cũng bắt đầu bằng 1

        if triangle:                  # Nếu không phải dòng đầu tiên (tức triangle không rỗng)
            last_row = triangle[-1]   # Lấy dòng trước đó
            for j in range(len(last_row) - 1):                # Lặp qua các cặp phần tử liền kề
                row.append(last_row[j] + last_row[j + 1])     # Tính tổng và thêm vào dòng mới
            row.append(1)             # Dòng nào cũng kết thúc bằng 1

        triangle.append(row)          # Thêm dòng vừa tạo vào tam giác

    for row in triangle:              # In từng dòng trong tam giác Pascal
        print(row)