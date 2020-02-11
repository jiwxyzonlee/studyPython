#readlines02

f = open("C:\doit\새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)   #data를 파일 객체 f에 씀
f.close()

print("정상적으로 파일이 생성되었습니다.")


#f = open("C:\doit\새파일.txt", 'r')
#lines = f.readlines()
#for line in lines:
#    print(line)
#f.close()



fname = input("파일명을 입력하세요: ")
f = open("C:\doit\{0}.txt" .format(fname), 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


#f = open("C:\doit\새파일.txt", 'r')
#while True:
#    line = f.readline()
#    if not line: break
#    print(line)
#f.close()
