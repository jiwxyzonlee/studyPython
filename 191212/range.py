##1

#result = [i for i in range(1, 101)]

#print (result)

##1.1

#i = 0
#while i  < 100:
#    i = i + 1
#    print(i)
    

##2

#A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

#total = 0

#for x in A:
#    total = total + x
#mean = total /(len(A))
        
#print(mean)


##3
#numbers = [1, 2, 3, 4, 5]
#result = []

#for n in numbers:
#    if n % 2 == 1:
#        result.append(n*2)
#print(result)


#result = [n * 2 for n in numbers if n % 2 == 1]
#print(result)


##4
##내 답
#for treeHit in range(0, 10):
#    treeHit = treeHit +1
#    print("나무를 %d번 찍었습니다." %treeHit)
#
#    if treeHit == 10:
#        print("나무가 넘어갑니다.")


##바람직한 답
#for treeHit in range(1, 11):
#    print("나무를 %d번 찍었습니다." %treeHit)
#
#    if treeHit == 10:
#        print("나무가 넘어갑니다")



#5
while True:

     num = list(input("숫자를 여러개 입력하세요:"))

     for i in num:
          i = int(i)
          print("*" * i )


          


#while로 한 답



