import turtle

a = 1
b = 1
c = 1

bob = turtle.Turtle()
scr = turtle.Screen()

scr.title("3 FLOWERS")
scr.setup(650, 300)
scr.bgcolor("#a8dadc")

bob.speed(0)


def go_to(x, y):
    bob.pu()
    bob.goto(x, y)
    bob.pd()


def draw_flower(i, color1, color2):
    bob.color(color1, color2)
    bob.begin_fill()
    while i <= 36:
        bob.fd(150)
        bob.lt(170)
        i += 1
    bob.end_fill()


go_to(125, 0)
draw_flower(a, "blue", "cyan")

go_to(-75, 0)
draw_flower(b, "red", "yellow")

go_to(-275, 0)
draw_flower(c, "#7400b8", "#f2cc8f")


turtle.done()
