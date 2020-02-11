#exception_test.py

import traceback                          #traceback 모듈 호출
#예외 상황 테스트를 위한 함수 선언
def exception_test():
    print("[1] Can you add 2 and '2' in python?")
    try:                                            #try문 선언
        print("[2] Try it~!", 2 + '2')  #TypeError 발생
    except TypeError:                      #예외 처리
        print('[2] I got TypeError! Check below!')    #에러 메시지 출력
        traceback.print_exc()                                   #트레이스백 메시지 출력
    
    print("[3 It's not possible to add integer and string together.")

exception_test()
