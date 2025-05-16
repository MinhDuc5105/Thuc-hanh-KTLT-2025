def binary_search(arr, value):
    left, right = 0, len(arr) - 1  # Đặt biến left ở đầu mảng, right ở cuối mảng

    while left <= right:  # Lặp khi còn khoảng tìm kiếm
        mid = (left + right) // 2  # Tính chỉ số ở giữa

        if arr[mid] == value:
            return True  # Nếu tìm thấy phần tử đúng thì trả về True

        elif arr[mid] < value:
            left = mid + 1  # Nếu giá trị ở giữa < cần tìm → loại bên trái, giữ bên phải

        else:
            right = mid - 1  # Nếu giá trị ở giữa > cần tìm → loại bên phải, giữ bên trái

    return False  # Nếu hết vòng lặp mà không tìm thấy thì trả về False