print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def file_read_from_head(fname, nlines) :
    from itertools import islice
    with open (fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('D:/pt/name.txt  ',2)