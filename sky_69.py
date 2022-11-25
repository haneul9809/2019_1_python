import turtle
t=turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("","몇각형을 원하시나요?")
n=int(s)

a=turtle.textinput("","변의 길이를 지정하세요.")
len=int(a)

for i in range(n):
    t.forward(len)
    t.left(360/n)
