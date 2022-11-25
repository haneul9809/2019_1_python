import turtle
t=turtle.Turtle()

def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)
        
def drawit(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color("green")
    square(90)
    t.end_fill()

s=turtle.Screen()
s.onscreenclick(drawit)
