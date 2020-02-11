#writedata.py


f = open("C:\doit\새파일.txt", 'w')

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)   #data를 파일 객체 f에 씀
f.close()

print("정상적으로 파일이 생성되었습니다.")
