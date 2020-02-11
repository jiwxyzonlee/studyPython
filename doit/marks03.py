marks = [90, 25, 67, 45, 80]

#range 이용하기
#아까와 달리 변수조건(number=0) 쓸 필요 없음
#marks함수, number함수 연결해준 거라고 생각하면 됨

for number in range(len(marks)):
    
    if marks[number]  < 60:
        continue
    print("%d번 학생은 합격입니다." %(number+1))
