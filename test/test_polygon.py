from pyleap import *

window.set_size(600, 600)

t1 = Polygon(200, 100, 400, 100, 350, 300, 250, 300, "gray")
t2 = Polygon(300, 200, 500, 200, 450, 500, 350, 500, 200, 600)

def Loop(dt):
    window.clear()

    t1.draw()
    t2.rotation += 1
    t2.draw()

    p = t2.collide(t1)
    if p:
        Point(p[0], p[1], color="red", point_size=5).draw()


repeat(Loop)

run()