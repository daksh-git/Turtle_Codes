import turtle
import time

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)


# Creating a pen:
bob = turtle.Turtle()
bob.hideturtle()
bob.speed(0)
bob.pensize(3)


def draw_dials(hour_rn, min_rn, sec_rn):
    bob.color('#e76f51')
    bob.setheading(0)
    for i in range(12):
        bob.pu()
        bob.fd(220)
        bob.pd()
        bob.fd(25)
        bob.pu()
        bob.bk(245)
        bob.rt(30)
    bob.pu()
    bob.goto(0, -245)
    bob.pd()
    bob.setheading(0)
    bob.circle(245)

    # Hour Hand:
    bob.pu()
    bob.goto(0, 0)
    bob.color('white')
    bob.setheading(90)
    angle_hr = (hour_rn / 12) * 360
    bob.rt(angle_hr)
    bob.pd()
    bob.fd(100)

    # Minute Hand:
    bob.pu()
    bob.goto(0, 0)
    bob.color('blue')
    bob.setheading(90)
    angle_min = (min_rn / 60) * 360
    bob.rt(angle_min)
    bob.pd()
    bob.fd(200)

    # Second Hand:
    bob.pu()
    bob.goto(0, 0)
    bob.color('yellow')
    bob.setheading(90)
    angle_sec = (sec_rn / 60) * 360
    bob.rt(angle_sec)
    bob.pd()
    bob.fd(170)
    bob.goto(0, 0)


while True:
    hr = int(time.strftime("%I"))
    mi = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_dials(hr, mi, sec)
    screen.update()
    screen.tracer(0)
    bob.clear()
