print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
str= input("Nhập vào: ")
dict = {}
for n in str:
    keys =  dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)