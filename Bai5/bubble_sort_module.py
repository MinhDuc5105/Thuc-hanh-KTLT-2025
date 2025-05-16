def bubbleSort(nlist):
    for i in range(len(nlist) - 1):  # Lặp qua từng lần "nổi bọt", tổng cộng n-1 lần
        for j in range(len(nlist) - 1 - i):  # So sánh các cặp liền kề trong phạm vi chưa sắp
            if nlist[j] > nlist[j + 1]:  # Nếu phần tử bên trái lớn hơn bên phải
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]  # Đổi chỗ chúng lại (swap)
    return nlist  # Trả về danh sách đã sắp xếp