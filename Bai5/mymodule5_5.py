def find_max(lst):  # Định nghĩa hàm find_max, nhận 1 danh sách lst làm tham số
    """Trả về phần tử lớn nhất trong danh sách"""
    max_val = lst[0]  # Giả sử phần tử đầu tiên là lớn nhất
    for item in lst:  # Duyệt qua từng phần tử trong danh sách
        if item > max_val:  # Nếu phần tử hiện tại lớn hơn max_val
            max_val = item  # Cập nhật max_val bằng phần tử đó
    return max_val  # Trả về giá trị lớn nhất tìm được

def sort_list(lst):  # Định nghĩa hàm sort_list, nhận 1 danh sách lst
    """Trả về danh sách đã sắp xếp tăng dần"""
    return sorted(lst)  # Dùng hàm sorted() để sắp xếp và trả về danh sách mới