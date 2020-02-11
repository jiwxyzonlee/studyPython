#sub_dir_search01.py

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        #os.listdir을 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있음
    #print(filenames)
        for filename in filenames:
        #print(filename) 정말 파일 이름만 나옴 $Recycle.Bin, bootTel.dat, Documents and Settings
            full_filename = os.path.join(dirname, filename) #파일 리스트는 파일 이름만 포함되어 있으므로
        #경로를 포함한 파일 이름을 구하기 위해서는 입력으로 받은 dirname을 앞에 덧붙여줘야 함
        #os.path.join 함수는 디렉터리와 파일 이름을 이어주는 전체 경로를 구해 줌
            #print(full_filename) C:/$Recycle.Bin, C:/bootTel.dat, C:/Documents and Settings
            if os.path.isdir(full_filename):
                search(full_filename)
        #os.path.isdir 함수는 full_filename이 디렉터리인지 파일인지 구분하기 위해 사용함
        #디렉터리일 경우 해당 경로를 입력받아 다시 search함수를 호출함 (재귀 호출)
                """
                해당 디렉터리의 파일이 디렉터리일 경우,
                다시 search함수를 호출하면 해당 디렉터리의 하위 파일을 다시 검색하기 시작하므로
                결국 모든 파일들을 검색할 수 있게 됨 >>>다 검색됨...(파일 안 멈춤)
                """

            else:
                ext = os.path.splitext(full_filename)[-1]
        #i = os.path.splitext(full_filename)
        #print(i)  #('C:/$Recycle', '.Bin'), ('C:/bootTel', '.dat'), ('C:/swapfile', '.sys'), ...
                if ext == '.py':
                    print(full_filename)
         #해당 이름의 확장이름 출력 ([-1]은 맨 마지막값
        #print(ext)  # .Bin,  .dat,  .sys, .log, ...
    except PermissionError:
        pass
        
           
#“C:/” 디렉터리에 파이썬 파일이 없다면 아무것도 출력되지 않음
search("C:/") #search라는 함수를 만들고 시작 디렉터리를 입력 받도록 코드를 작성함

