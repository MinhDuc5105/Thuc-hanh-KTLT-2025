print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def lay_nguyen_to_duoi_1trieu():                   # Định nghĩa hàm để lấy các số nguyên tố nhỏ hơn 1 triệu
    limit = 1_000_000                              # Giới hạn trên: 1 triệu (có thể viết là 1000000)
    is_prime = [True] * limit                      # Tạo danh sách `is_prime` gồm `limit` phần tử đều là True
    is_prime[0] = is_prime[1] = False              # 0 và 1 không phải số nguyên tố → gán False

    for i in range(2, int(limit ** 0.5) + 1):  # Duyệt từ 2 đến căn bậc hai của limit (tối ưu sàng Eratosthenes)
        if is_prime[i]:  # Nếu i là số nguyên tố
            for j in range(i * i, limit, i):  # Đánh dấu các bội số của i bắt đầu từ i*i
                is_prime[j] = False  # Không phải nguyên tố → gán False

    return tuple(i for i, prime in enumerate(is_prime) if prime)
    # Duyệt qua danh sách `is_prime`, lấy chỉ số i nếu giá trị tại đó là True (nghĩa là số nguyên tố)
    # Kết quả được chuyển thành tuple

P = lay_nguyen_to_duoi_1trieu()                    # Gọi hàm và gán tuple kết quả vào biến P
print("Số lượng số nguyên tố nhỏ hơn 1 triệu là:", len(P))     # In ra số lượng phần tử trong tuple P
print("10 số nguyên tố đầu tiên:", P[:10])         # In ra 10 số nguyên tố đầu tiên từ tuple P
