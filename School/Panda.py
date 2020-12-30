import turtle as bob

bob.speed(0)


def draw_ears():
    bob.speed(6)
    bob.color('black')
    bob.begin_fill()
    bob.circle(75)
    bob.end_fill()


def draw_face():
    bob.speed(7)
    bob.color('white')
    bob.begin_fill()
    bob.circle(150)
    bob.end_fill()
    bob.pensize(2)
    bob.speed(6)
    bob.color('black')
    bob.circle(150)


def draw_eyes():
    bob.color('black')
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()
    bob.lt(90)
    bob.fd(10)
    bob.rt(90)
    bob.color('white')
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()


def draw_nose():
    bob.speed(6)
    bob.color('black')
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    bob.pensize(2)
    bob.setheading(270)
    bob.circle(20, 180)
    bob.setheading(180)
    bob.speed(0)
    bob.pu()
    bob.fd(80)
    bob.pd()
    bob.speed(6)
    bob.setheading(270)
    bob.circle(20, 180)


def locate_eye_1():
    bob.pu()
    bob.lt(90)
    bob.fd(150)
    bob.rt(90)
    bob.fd(55)
    bob.pd()


def locate_eye_2():
    bob.pu()
    bob.bk(110)
    bob.rt(90)
    bob.fd(10)
    bob.lt(90)
    bob.pd()


def locate_nose():
    bob.speed(0)
    bob.pu()
    bob.goto(0, -200)
    bob.lt(90)
    bob.fd(70)
    bob.setheading(0)
    bob.pd()


def go_to_start():
    bob.speed(0)
    bob.pu()
    bob.goto(0, -200)
    bob.pd()


def locate_ear_1():
    bob.speed(0)
    bob.pu()
    bob.goto(0, -200)
    bob.circle(150, 115)
    bob.setheading(0)
    bob.pd()


def locate_ear_2():
    bob.speed(0)
    bob.pu()
    bob.goto(0, -200)
    bob.circle(150, 115 + 130)
    bob.setheading(0)
    bob.pd()


locate_ear_1()
draw_ears()
locate_ear_2()
draw_ears()
go_to_start()
draw_face()
locate_eye_1()
draw_eyes()
locate_eye_2()
draw_eyes()
locate_nose()
draw_nose()

bob.done()
