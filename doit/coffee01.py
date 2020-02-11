button = 0

button = int(input("1.아메리카노\n2.카페라떼\n3.카푸치노\n4.바리스타추천\n\n어떤 커피를 드릴까요?"))

print()
print("#1. 뜨거운 물을 준비한다." )
print("#2. 종이컵을 준비한다.")

def coffee_machine(button):
    if button == 1:
        return "아메리카노"
    elif button == 2:
        return "카페라떼"
    elif button == 3:
        return "카푸치노"
    else:
        return "#아무 음료"
    

result = coffee_machine(button)
print("#3. {0}번 {1}를 탄다" .format(button, result))
print("#4. 물을 붓는다.")
print("#5. 스푼으로 젓는다.")

print()
print("손님~커피 여기 있습니다.")






#coffee_machine = lambda button: "아메리카노를 탄다" if button == 1 elif
