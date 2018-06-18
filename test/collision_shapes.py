from pyleap import *


rect = Rectangle(100, 100, 200, 50)
circle = Circle(200, 200, 50)


p = Point(point_size=10, color="red")
circle.transform.scale_x = 2


def draw(dt):
    window.clear()
    c = rect.collide(circle)
    rect.transform.rotation += 1
    circle.transform.rotation += 1
    rect.stroke()
    circle.stroke()
    if(c):
        p.x = c[0]
        p.y = c[1]
        p.draw()


def move():
    circle.x = mouse.x
    circle.y = mouse.y

mouse.on_move(move)

schedule_interval(draw)

run()
