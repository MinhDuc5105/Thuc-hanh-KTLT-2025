print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
input_file=open(r'D:\pt\sh.txt','r')
for line in input_file:
    i =len(line)
    s = ' '
    while(i>=1):
        s=s+line[i-1]
        i=i-1
    print(s)
input_file.close()