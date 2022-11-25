import turtle
t=turtle.Turtle()
t.shape("turtle")
i=0
a=0

while i<5:
    t.forward(50)
    t.right(144)
    i=i+1

t.penup()
t.goto(100,0)
t.pendown()

while i<5:
    t.forward(50)
    t.right(144)
    i=i+1

t.penup()
t.goto(200,0)
t.pendown()

while i<5:
    t.forward(50)
    t.right(144)
    i=i+1
