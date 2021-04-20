import turtle
import j
t = turtle.Turtle()
t.speed(0)
i = 1
t.clear()
colours=["red","orange"]
while True:
    t.width(5)
    t.forward(i)
    t.left(100)
    t.color(colours[i%2])
    i += 1
