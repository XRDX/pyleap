from pyleap import *

window.set_caption("LeapLearner")

bg = Rectangle(0, 0, window.width, window.height, color="orange")
r = Rectangle(color=(125, 125, 0))
line1 = Line(100, 200, 300, 400, 'pink')
tri = Triangle(200, 100, 300, 100, 250, 150, "green")
c = Circle(200, 200, 50, "red")
txt = Text('Hello, world')


def update(dt):
    r.x += 1
    r.y += 1
    c.x += 1


def draw(dt):
    # update()
    window.clear()
    bg.draw()

    rectangle(100, 100, 50, 25, 'pink')
    r.stroke()
    line1.draw()
    tri.stroke()
    c.draw()
    txt.draw()


def startMove():
    schedule_interval(update, 1 / 60)


mouse.on_press(startMove)


schedule_interval(draw, 1 / 60)
run()
