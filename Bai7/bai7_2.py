print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")
k = open(r'D:\pt\name.txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range (0,len(line)):
        char += 1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc,lc=wc+1,lc+1
print('So ki tu la %d\n so tu la %d\n so dong la %d'%(char,wc,lc))