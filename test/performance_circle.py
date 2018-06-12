from pyleap import *


circles = []


def draw(dt):
    for c in circles:
        c.draw();

    print(len(circles))


def new_circle():
    circles.append(Circle(mouse.x, mouse.y))


mouse.on_move(new_circle)

schedule_interval(draw)
run()