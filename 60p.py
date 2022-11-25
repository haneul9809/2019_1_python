import turtle
t=turtle.Turtle()
t.shape("turtle")

radius=100

t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
t.circle(radius)

t.penup()
t.goto(0,-200)
t.pendown()

x=100
radius=50

t.circle(radius)
t.fd(x)
t.circle(radius)
t.fd(x)
t.circle(radius)
