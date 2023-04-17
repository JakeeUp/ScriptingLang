import turtle
t = turtle.Turtle()
t.speed(0)
radius = 100

for i in range(-radius, radius):
    x = i
    y = (-1) * ((radius**2 - x**2)**0.5)
    t.goto(x, y)
    t.dot(2, 'black')

for i in range(radius, -radius, -1):
    x = i
    y = ((radius**2 - x**2)**0.5)
    t.goto(x, y)
    t.dot(2, 'black')

t.hideturtle()

turtle.done()
