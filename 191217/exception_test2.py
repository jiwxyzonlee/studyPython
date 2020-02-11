#exception_test2.py

#예외 상황 테스트를 위한 함수 선언
def exception_test2(file_path):
    try:                                            #try문 선언
        f = open(file_path, 'r')  
    except IOError:                      #예외 처리
        print('cannot open!', file_path)    #에러 메시지 출력       
    else:
        print('File has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print('I just tried to read this file.', file_path)

exception_test2('C:/doit/mod.py')
