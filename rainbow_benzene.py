import turtle

# declaring all the colors
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'deeppink']

t = turtle.Pen()  # creating the object
t.speed(15)

turtle.bgcolor('#000')
turtle.title("Turtle Rainbow Benzene")

for x in range(360):
    t.pencolor(colors[x % 7])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
