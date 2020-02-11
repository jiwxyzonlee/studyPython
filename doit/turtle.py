import random
import turtle

t = turtle.Turtle()
t.shape("turtle")

scr = turtle.Screen()
scr.setup(600, 600)

while True:
    coin = random.randint(0, 1)
    if coin == 0:
        t.left(90)  #coin 값이 0이면 왼쪽 방향으로 90도 회전
    else:
        t.right(90)  #coin 값이 1이면 오른쪽 방향으로 90도 회전

    t.forward(50)   #거북이 위치가 창 밖에 나가면 멈춤
    if t.xcor() <= -300 or t.xcor() >= 300:
        break
    if t.ycor() <= -300 or t.ycor() >= 300:
        break
