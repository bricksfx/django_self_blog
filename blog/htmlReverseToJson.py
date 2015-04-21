#coding=utf-8
def reverse(file1, file2):
    f = open(file1, 'r')
    f2 = open(file2, 'w')
    for eachline in f:
        f2.write("'" + eachline[0:-1] + "' +" + "\n")
    f.close()
    f2.close()


