import turtle

tt = turtle.Turtle()

tt.speed(10)

tt.pu()
tt.goto(-50, 120)
tt.pd()

# BORDER-COLOR:


tt.color("#f4a261")

tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)


# FILL-COLOR:

tt.color("blue")

tt.penup()
tt.forward(50)
tt.pendown()

tt.begin_fill()
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.end_fill()
tt.left(90)
tt.forward(100)

# TWO-IN-ONE:

tt.color("#d62828", "#f6bd60")

tt.penup()
tt.forward(50)
tt.pendown()

tt.begin_fill()
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.left(90)
tt.forward(100)
tt.end_fill()


turtle.done()