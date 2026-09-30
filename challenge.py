import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def triangle(length, level):
    if level == 0:
        for i in range(3):
            t.forward(length)
            t.left(120)

    else:
        triangle(length / 2, level - 1)
        
        t.forward(length / 2)
        triangle(length / 2, level - 1)

        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)

        triangle(length / 2, level - 1)

        t.left(60)
        t.backward(length / 2)
        t.right(60)

triangle(300, 5)

turtle.done()