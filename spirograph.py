# This is a custom module we've made.
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle
import math
import random


def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def draw_triangle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size*3)
        turtle.left(120)
    turtle.end_fill()
    turtle.setheading(0)


def draw_square(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size*2)
        turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)


def draw_star(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size*2)
        turtle.right(144)
        turtle.forward(size*2)
    turtle.end_fill()
    turtle.setheading(0)


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Spirograph')
s = turtle.Turtle()
s.speed('fastest')
s.color('pink')
rotate = int(180)


def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size-4


def circle(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


circle(s, 200, 10)
t1 = turtle.Turtle()
t1.speed(0)
t1.color('#DE3163')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-10


def circle(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


circle(t1, 160, 10)
t2 = turtle.Turtle()
t2.speed(0)
t2.color('DeepPink')
rotate = int(80)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-5


def circle(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


circle(t2, 120, 10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('PaleVioletRed')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-19


def circle(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


circle(t3, 80, 10)
t4 = turtle.Turtle()
t4.speed(0)
t4.color('IndianRed')
rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-20


def circle(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360/repeat)


circle(t4, 40, 10)

turtle.done()
