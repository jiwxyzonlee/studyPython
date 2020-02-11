#  coding: utf-8 #
"""
Created on Fri Dec 12 2019
@Jiwon Lee

"""

button = 0
portion = 0
bakery = 0
count = 10

def cup_hold(portion):
     if portion == 1: return "한"    
     elif portion == 2: return "두"
     elif portion ==3: return "세"
     else: return "네"
cup = cup_hold(portion)

def coffee_machine(button):
    if button == 1: return "아메리카노"
    elif button == 2: return "카페라떼"
    elif button == 3: return "카푸치노"
    else: return "오늘의 커피"
result = coffee_machine(button)

def cake_case(bakery):
    if bakery == 1: return "당근케이크"
    elif bakery == 2: return "치즈케이크"
    elif bakery == 3: return "딸기타르트"
    else: return "무화과스콘"
snack = cake_case(bakery)

def routine(money, price):
    while True:
        if money - price < 0:
            money1 = int(input("금액이 부족합니다. \n다시 적어주세요: "))
            if money1 - price < 0:
                print ("나가주세요, 손님")
                print()
                break
        elif money - price > 0:
            print1 = print(money, "원 받았습니다.", money - price, "원 거슬러 드리겠습니다.")
            return {print1, print_all()}
        else:
             print2 = print("감사합니다 손님.")
             return{print2, print_all()}
 
def print_all():
        print()
        print("#1. 뜨거운 물 {0} 잔을 준비한다." .format(cup))
        print("#2. 종이컵을 {0} 개를  준비한다." .format(cup))
        print("#3. {0}번 {1}를 탄다" .format(button, result))
        print("#4. 물을 붓는다.")
        print("#5. 스푼으로 젓는다.")
        print("#6. {0}를 접시에 내놓는다." .format(snack))
        print()
        print("{0}님 주문하신 {1} {2} 잔과  {3} 나왔습니다!!!!" .format(nick, result, cup, snack))
        print()
        
     

while True:

 button = int(input("1.아메리카노\n2.카페라떼\n3.카푸치노\n4.바리스타추천\n\n모든 음료 4천원\n어떤 커피를 드릴까요? "))
 print()
 portion = int(input("1잔, 2잔, 3잔, 4잔\n몇 잔 드릴까요? "))
 print()
 bakery = int(input("또 필요한 건 없으실까요?\n1. 당근케이크, 2. 치즈케이크, 3. 딸기타르트, 4. 무화과스콘 : "))
 print()
 nick = input("손님 잔에 뭐라고 적어드릴까요? ")
 print()
 price = portion * 4000
 print("총", price, "원입니다. 제과류는 서비스입니다")
 print()
 money = int(input("내실 돈을 적어주세요: "))
 print()
 
 cup_hold(portion)
 coffee_machine(button)
 cake_case(bakery)
 routine(money, price)
 
 count = count - 1
 if count == 0:
     print("재고가 부족한 관계로 영업을 종료합니다. 감사합니다.")
     break
 else:
     print("다음 손님, 오래 기다리셨습니다.")
     print()







