import turtle
import random
import math

player=turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.up()
player.speed(0)
scree=player.getscreen()

asteroids=[]
for i in range(10):
    a1=turtle.Turtle()
    a1=color("red")
    a1.shape("circle")
    a1.up()
    a1.speed(0)
    a1.goto(random.radint(-300,300),random.randint(-300,300))

def turnleft():
    player.left(30)
def turnright():
    player.right(30)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.listen()

def play():
    player.forward(2)
    for a in asteroids:
        a.right(random.randint(-180,180))
        a.forward(2)
    screen.ontimer(play,10)
screen.ontimer(play,10)
