import turtle

bob = turtle.Turtle()
bob.speed(5)

square_length = 200
sides = 1
color_index = 0

colors = ["red", "orange", "yellow", "green", "blue"]

while square_length >= 40:
    while color_index <= 4:
        bob.color("black", colors[color_index])
        bob.begin_fill()
        while sides <= 4:
            bob.fd(square_length)
            bob.lt(90)
            sides += 1
        bob.end_fill()
        color_index += 1
        sides = 1
        square_length = square_length - 40

turtle.done()
