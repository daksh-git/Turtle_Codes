from turtle import *

side = 480
speed(0)

pu()
goto(-(side / 2), -(side / 2))
pd()


def draw_triangle(length, angle):
    for a in range(3):
        fd(length)
        lt(angle)


draw_triangle(side, 120)

fd(side / 2)
lt(60)

draw_triangle(side / 2, 120)

for b in range(3):
    fd(side/4)
    rt(60)
    draw_triangle(side/4, -120)
    lt(60)
    fd(side / 4)
    lt(120)



done()
