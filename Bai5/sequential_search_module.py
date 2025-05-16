def Sequential_Search(dlist, item):  # Định nghĩa hàm tìm kiếm tuần tự, nhận danh sách dlist và giá trị cần tìm item
    for index, value in enumerate(dlist):  # Duyệt qua từng phần tử trong dlist, lấy cả chỉ số (index) và giá trị (value)
        if value == item:  # Nếu giá trị hiện tại bằng với item cần tìm
            return (True, index)  # Trả về True và vị trí tìm thấy
    return (False, -1)  # Nếu không tìm thấy, trả về False và -1