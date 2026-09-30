import turtle

t = turtle.Turtle()

def draw_polygon(sides):
    angle = 360 / sides

    for i in range(sides):
        t.forward(100)
        t.right(angle)

draw_polygon(5)
turtle.done()