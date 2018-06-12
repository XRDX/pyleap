from pyleap import *

bg = Rectangle(0, 0, window.width, window.height, color="white")
r = Rectangle(color=(125, 125, 0))
line1 = Line(100, 200, 300, 400, 2, 'pink')
tri = Triangle(200, 100, 300, 100, 250, 150, "green")
c2 = Circle(200, 200, 50, "#ffff00")
c = Circle(200, 200, 100, "red")
txt = Text('Hello, world')


def update(dt):
    r.x += 1
    r.y += 1
    c.x += 1


def draw(dt):
    # update()
    window.clear()
    bg.draw()

    Rectangle(100, 100, 50, 25, 'pink').draw()
    r.stroke()
    line1.draw()
    tri.stroke()
    c.draw()
    c2.draw()
    txt.draw()


def start_move():
    schedule_interval(update)

def stop_move():
    unschedule(update)


mouse.on_press(start_move)
mouse.on_release(stop_move)


schedule_interval(draw)
run()
