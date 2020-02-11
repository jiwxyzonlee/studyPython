#sub_dir_search.py

import os

def search(dirname):
    filenames = os.listdir(dirname)  #os.listdir을 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있음
    #print(filenames)
    for filename in filenames:
        #print(filename)
        full_filename = os.path.join(dirname, filename) #파일 리스트는 파일 이름만 포함되어 있으므로
        #경로를 포함한 파일 이름을 구하기 위해서는 입력으로 받은 dirname을 앞에 덧붙여줘야 함
        #os.path.join 함수는 디렉터리와 파일 이름을 이어주는 전체 경로를 구해 줌
        #i = os.path.splitext(full_filename)
        #print(i)  #('C:/$Recycle', '.Bin'), ('C:/bootTel', '.dat'), ('C:/swapfile', '.sys'), ...
        ext = os.path.splitext(full_filename)[-1]  #해당 이름의 확장이름 출력 ([-1]은 맨 마지막값
        #print(ext)  # .Bin,  .dat,  .sys, .log, ...
        if ext == '.py':
            print(full_filename)
    

search("C:/") #search라는 함수를 만들고 시작 디렉터리를 입력 받도록 코드를 작성함

