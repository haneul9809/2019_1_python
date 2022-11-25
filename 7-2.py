import turtle
import random

def draw_maze(x,y):
    for i in range(2):
        t.up()
        if i==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.down()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)
    

def turn_left():
    t.lt(10)
    t.fd(10)

def turn_right():
    t.rt(10)
    t.fd(10)

t=turtle.Turtle()
screen=turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300,200)
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")

t.up();
t.goto(-300,250)
t.speed(1)
t.down();

screen.listen()
screen.mainloop()
