from leap import *

canvas.set_caption("LeapLearner")

bg = Rectangle(0, 0, canvas.width, canvas.height, color="white")
r = Rectangle(color=(125, 125, 0))
line1 = Line(100, 200, 300, 400, 'pink')
t = Triangle(200, 100, 300, 100, 250, 150, "green")
c = Circle(200, 200, 50, "red")


def update(dt):
    canvas.clear()
    bg.draw()

    rectangle(100, 100, 50, 25, 'pink')

    r.x += 1
    r.y += 1
    r.stroke()

    line1.draw()

    t.stroke()

    c.x += 1
    c.draw()


setInterval(update, 1 / 60)
run()
