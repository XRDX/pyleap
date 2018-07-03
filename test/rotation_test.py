from pyleap import *

bg = Rectangle(0, 0, window.width, window.height, color="white")
c = Circle(200, 200, 100, "red")
c.transform.scale_y = 0.5


def update(dt):
    c.x += 1
    c.rotation -= 1

def draw(dt):
    # update()
    window.clear()
    bg.draw()
    c.draw()


repeat(draw)
repeat(update)

run()
