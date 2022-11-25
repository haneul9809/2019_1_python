import turtle


t=turtle.Turtle()
t.shape("turtle")

def n_polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)

for i in range(10):
    t.fillcolor("yellow")
    t.begin_fill()
    t.left(20)
    n_polygon(6,100)
    t.end_fill()
