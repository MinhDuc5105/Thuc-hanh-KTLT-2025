print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
import math

def chuvihinhtron(r):
    return 2 * math.pi * r

def dientichhinhtron(r):
    return math.pi * (r ** 2)

r = int(input("Nhập r: "))
print("Chu vi:", chuvihinhtron(r))
print("Diện tích:", dientichhinhtron(r))


