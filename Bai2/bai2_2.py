print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import math;
x1=int(input ("Nhập x1: "))
y1=int(input("Nhập y1: "))

x2=int(input ("Nhập x2: "))
y2=int(input("Nhập y2: "))

d1= (x2 - x1) * (x2 - x1);
d2 = (y2 - y1) * (y2 - y1);
res = math.sqrt(d1+d2)
print ("Khoảng cách 2 điểm là:", res);