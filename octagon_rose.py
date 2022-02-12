import turtle

# declaring all the colors
colors = ['#A30051', '#A30051', '#A30051', '#A30051', '#A30051', '#A30051']

t = turtle.Pen()  # creating the object
t.speed(100)
turtle.title("Turtle Octagon Rose")

turtle.bgcolor('#000')  # background color

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(int(x/100) + 1)
    t.forward(x)
    t.left(49)

turtle.done()
