#readlines03
#sys


import sys

f = open("C:\doit\새파일.txt", 'r')
lines = f.readlines()
for i in lines:
    print(i, end = '')
f.close()

#args = sys.argv[1:]
#for i in args:
#    print(i)




