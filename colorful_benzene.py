import turtle

# declaring all the colors
colors = ['red', 'deeppink', 'blue', 'green', 'orange', 'yellow']

t = turtle.Pen()  # creating the object
t.speed(10)
turtle.title("Turtle Colorful Benzene")

turtle.bgcolor('#000')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
