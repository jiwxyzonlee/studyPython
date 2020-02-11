#tabto4.py


import sys

#C:\doit>python tabto4.py a.txt b.txt
#sys모듈에서 제공하는 sys.argv[0]은 tabto4.py

src = sys.argv[1]  #커맨드창 첫번째 변수 a.txt
dst = sys.argv[2] #커맨드창 두번째 변수 b.txt

f = open(src)  #a.txt 열기(open default는 rt-read and text, 텍스트모드)
tab_content = f.read()  #read()는 파일 입력함
f.close()

space_content = tab_content.replace("\t", " "*4)  #tab을 공백 네 번으로 바꾸기

f = open(dst, 'w')  #b.txt 새로 쓰기 (커맨드 창에 실행 뒤에는 doit에 b.txt 생김)
f.write(space_content) #b.txt에 탭 띄워쓰기가 space로 바뀌어 있는 거로 씌워짐
f.close()


