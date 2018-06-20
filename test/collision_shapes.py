from pyleap import *


rect = Rectangle(100, 100, 200, 50)
rect2 = Rectangle(100, 100, 200, 50)
circle = Circle(200, 200, 50)


p = Point(point_size=10, color="red")
circle.transform.scale_x = 2
# rect.transform.set_anchor_rate(1, 1)


def draw(dt):
    window.clear()
    
    rect.rotation += 1
    circle.rotation -= 1
    rect.stroke()
    rect2.stroke()
    circle.stroke()

    c = rect.collide(circle)
    if(c):
        p.x = c[0]
        p.y = c[1]
        p.draw()

    c = rect2.collide(rect)
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
