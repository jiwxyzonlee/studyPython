my_id = "python"
my_password = "1234"
count = 5

while True:
    
    ID = input("아이디를 입력하세요 : ")
    PSSWD = input("패스워드를 입력하세요 : ")
    count = count - 1

    if ID == "python" and PSSWD == "1234":
        print("** 정상적으로 로그인에 성공했습니다 **")
        break

    elif ID != "python" and PSSWD == "1234":
        print("** 아이디가 틀렸습니다 **")
     
    elif ID == "python" and PSSWD != "1234":
        print("** 패스워드가 틀렸습니다 **")
        
    else:
        print("** 아이디와 패스워드가 틀렸습니다 **")

    if count == 0:
        print(" ** 입력을 5번 실패하셨습니다. 입력을 종료합니다 **")
        break
       



