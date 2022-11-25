import turtle


def draw_olympic_symbol():
    positions=[[0,0,"blue"],[-120,0,"purple"],[60,60,"red"],[-60,60,"yellow"],[-180,60,"green"]]
    for x,y,c in positions:
        t.up()
        t.goto(x,y)
        t.down()
        t.color(c,c)
        t.begin_fill()
        t.circle(60)
        t.end_fill()


t=turtle.Turtle()
draw_olympic_symbol()
