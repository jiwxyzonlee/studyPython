#dbtest01

import sqlite3

#연결자 생성
con = sqlite3.connect("C:/sqlite/naverDB")

#커서 생성(데이터를 주고받을 통로 생성)
cur = con.cursor()

#테이블 생성  sep= ,(콤마로 구분)
cur.execute("DROP TABLE userTable")
cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(15), birthYear int)")

#데이터 입력
#cur.execute("INSERT INTO userTable VALUES('John', 'john Bann', 'john@naver.com', 1990)")
#cur.execute("INSERT INTO userTable VALUES('kim', 'Kim Chi', 'kim@daum.net', 1992)")
#cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Pal', 'lee@paran.com', 1988)")
#cur.execute("INSERT INTO userTable VALUES('park', 'Park Su', 'park@gmail.com', 1980)")

#입력한 데이터 저장
con.commit()

#데이터 베이스 닫기
con.close()
