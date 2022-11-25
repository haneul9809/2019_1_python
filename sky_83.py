import turtle
t=turtle.Turtle()

def draw(x,y):
    t.goto(x,y)

t.shape("turtle")
t.pensize(10)
s=turtle.Screen()
s.onscreenclick(draw)

s.onkey(t.penup,"Up")
s.onkey(t.pendown,"Down")
s.listen()
