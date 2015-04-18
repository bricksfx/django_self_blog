#coding=utf-8
def reverse(filename):
    f = open(filename, 'r')
    f2 = open('newfile.txt', 'w')
    for eachline in f:
        f2.write("'" + eachline[0:-1] + "' +" + "\n")
    f.close()
    f2.close()
reverse("test.txt")

