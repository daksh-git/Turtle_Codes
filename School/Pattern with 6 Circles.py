import turtle as bob

bob.speed(0)
initial_radius = 120

bob.bgcolor("black")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", ""]

a = 0
while a <= 7:
    bob.color(colors[a])
    for i in range(6):
        bob.circle(initial_radius)
        bob.rt(60)
    initial_radius -= 10
    a += 1

bob.done()