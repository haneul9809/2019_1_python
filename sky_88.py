import turtle
import random

screen=turtle.Screen()

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()

t1.color("pink")
t1.shape("turtle")
t1.pensize(5)
t1.shapesize(5)

t2.color("blue")
t2.shape("turtle")
t2.pensize(5)
t2.shapesize(5)

t3.color("green")
t3.shape("turtle")
t3.pensize(5)
t3.shapesize(5)

t1.up()
t1.goto(-300,0)

t2.up()
t2.goto(-300,-100)

t3.up()
t3.goto(-300,-200)

t1.down()
t2.down()
t3.down()
t1.speed(1)
t2.speed(1)
t3.speed(1)

for i in range(100):
    d1=random.randint(1,100)
    t1.forward(d1)
    d2=random.randint(1,100)
    t2.forward(d2)
    d3=random.randint(1,100)
    t3.forward(d3)
    
