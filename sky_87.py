import turtle
t=turtle.Turtle()
t.shape("turtle")

s=turtle.Screen();
s.bgcolor("skyblue");

x=0
y=0
def draw_snowman(x,y):
    t.up()
    t.goto(x,y+110)
    t.down()
    t.circle(35)


