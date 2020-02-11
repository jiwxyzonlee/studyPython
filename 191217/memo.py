# memo.py

import sys

#C:\doit>python memo.py[0] –v[1] (메모내용)[2]

option = sys.argv[1]   #sys.argv[1]은 프로그램 실행 옵션 값임

#sys.argv는 프로그램 실행 시 입력된 값을 읽어 들일 수 있는 라이브러리임
#sys.argv[0]는 프로그램 이름인 memo.py이므로 만들려는 기능에는 필요 없음

if option == '-a':      #뒤에 새로 추가히기
    memo = sys.argv[2]      #sys.argv[2]는 메모 내용임
    f = open('memo.txt', 'a')
    f.write(memo)
    f.close()
elif option == '-v':    #조회하기
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
elif option == '-w':             #쓰기모드
    memo = sys.argv[2]       #sys.argv[2]는 메모 내용임
    f = open('memo.txt', 'w')
    f.write(memo)
    f.close()
