# C:/doip/login02.py

my_id = "python"	#등록된 ID
my_psswd = "1234"	#등록된 Password

while True:
    in_id = input("아 이 디 : ")
    in_psswd = input("패스워드 : ")

    if in_id == my_id and in_psswd == my_psswd:
        print("정상적으로 로그인에 성공했습니다.")
        break
    elif in_id != my_id and in_psswd == my_psswd:
        print("아이디가 틀렸습니다. 확인 후, 다시 입력해 주세요.")
    elif in_id == my_id and in_psswd != my_psswd:
        print("패스워드가 틀렸습니다. 확인 후, 다시 입력해 주세요.")
    else:
        print("아이디와 패스워드가 틀렸습니다.")

