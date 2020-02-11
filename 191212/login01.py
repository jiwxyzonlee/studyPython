# C:/doit/login01.py

my_id = "python"		#등록된 ID
my_psswd = "1234"	#등록된 Password

in_id = input("아 이 디 : ")
in_psswd = input("패스워드 : ")

if in_id == my_id and in_psswd == my_psswd:
    print("정상적으로 로그인에 성공했습니다.")
elif in_id != my_id and in_psswd == my_psswd:
    print("아이디가 틀렸습니다.")
elif in_id == my_id and in_psswd != my_psswd:
    print("패스워드가 틀렸습니다.")
else:
    print("아이디와 패스워드가 틀렸습니다.")
