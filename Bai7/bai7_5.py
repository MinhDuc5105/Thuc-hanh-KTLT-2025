print("Sinh viên : Nguyễn Minh Đức")
print("Ma so SV : 235752020710030")


def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
            myfile.write("Python Exercises\n")
            myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read('D:/pt/name.txt')