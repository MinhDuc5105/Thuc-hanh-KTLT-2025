print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))

if a==0:
    if b== 0:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có 1 nghiệm x= ", -c/b)
else:
    denta = b ** 2 - 4 * a * c
    candenta = denta ** 0.5
    if denta > 0:
        x1 = (-b + candenta) / (2 * a)
        x2 = (-b - candenta) / (2 * a)
        print("Phương trình có 2 nghiệm phân biệt ","x1= ", x1 , "x2= ", x2)
    elif denta == 0:
        x = (-b )/ (2 * a)
        print("Phương trình có nghiệm kép x= ", x)
    else:
        print('Phương trình vô nghiệm')
