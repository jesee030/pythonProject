import turtleShow
t = turtleShow.Turtle()
t.speed(0)
i = 1
t.clear()
colours=["red"]
while True:
    t.width(5)
    t.forward(i)
    t.left(100)
    t.color(colours[i%7])
    i += 1
