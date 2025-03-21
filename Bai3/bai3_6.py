print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def get_sum(*num):
    dim = 0
    for i in num:
        dim += i
    return dim
result = get_sum(1, 2, 3, 4, 5)
print(result)