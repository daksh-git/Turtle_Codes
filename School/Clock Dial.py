import turtle as bob


bob.pensize(3)
screen = bob.getscreen()
screen.bgcolor('black')
bob.dot(8, 'white')
bob.shape('turtle')


def draw_dials():
    bob.color('#e76f51')
    bob.lt(60)
    for i in range(12):
        bob.pu()
        bob.fd(100)
        bob.pd()
        bob.fd(50)
        bob.pu()
        bob.fd(25)
        bob.pd()
        bob.write(str(i + 1), align='center', font=("Ariel", 12, "bold"))
        bob.pu()
        bob.bk(175)
        bob.rt(30)


def draw_ring():
    bob.color('#f4a261')
    bob.rt(150)
    bob.pu()
    bob.fd(200)
    bob.pd()
    bob.setheading(0)
    bob.circle(220)


draw_dials()
draw_ring()

bob.done()
