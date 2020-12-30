import turtle

tt = turtle.Turtle()
i = 0

tt.pu()
tt.goto(-330, 0)
tt.pd()

while i <= 66:
    tt.fd(5)
    tt.pu()
    tt.fd(5)
    tt.pd()

    i = i + 1

turtle.done()
