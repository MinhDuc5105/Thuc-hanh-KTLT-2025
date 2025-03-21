print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def benefit(t,n,k):
    r = (t/100)/12
    a = n * (1 + r * k)
    print("Tổng số tiền sau",k,"tháng là: ", a )
t = float(input("Lãi xuất tiết kiệm: "))
n = float(input("Số vốn ban đầu: "))
k = float(input("Số tháng gửi: "))
benefit(t,n,k)


