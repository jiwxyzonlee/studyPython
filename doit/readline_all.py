

#readline_all.py

f = open("C:\doit\새파일.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

"""
while True: 라는 무한 루프 안에서 f.readline()을 이용해 파일을 계속해서
한 줄씩 읽어 들이고, 만약 더 이상 읽을 줄이 없으면 break를 수행함
"""

while 1:
    data = input()
    if not data: break
    print(data)

