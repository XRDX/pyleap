from pyleap import *


circles = []
i=0

def update(c):
    c.x += c.xspeed
    c.y += c.yspeed
    if c.x > window.w:
        c.xspeed = -1
    elif c.x < 0:
        c.xspeed = 1
    if c.y > window.h:
        c.yspeed = -1
    elif c.y < 0:
        c.yspeed = 1

Circle.update = update

def draw(dt):
    window.clear()
    for c in circles:
        c.update()
        c.stroke()

    print(len(circles))
    window.show_fps()


def new_circle():
    global i
    i+=1
    c = Circle(mouse.x, mouse.y)
    c.color = hsl(i)
    c.xspeed = 1
    c.yspeed = 1
    circles.append(c)


mouse.on_move(new_circle)

repeat(draw)
run()