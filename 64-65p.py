import turtle
size=int(input("집의 크기는 얼마로 할까요? "))

t=turtle.Turtle()
t.shape("turtle")

t.fd(size)
t.right(90)
t.fd(size)
t.right(90)
t.fd(size)
t.right(90)
t.fd(size)

t.right(90)

t.fd(size)
t.left(120)
t.fd(size)
t.left(120)
t.fd(size)
