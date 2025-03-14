print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
a = 1
b =2
total = 0
print (a, end =" ")
while (a<= 4000000 -1 ):
    if a % 2 == 0:
        total =  total + a
    a , b =  b , a+b
    print (a, end =" ")
print ("\n Tổng các số nguyên tố trong dãy Fibonacci: " , total)