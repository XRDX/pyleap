from pyleap import *

window.set_size(600, 600)

t1 = Polygon(200, 100, 400, 100, 350, 300, 250, 300, "gray")


def Loop(dt):

    t1.draw()


repeat(Loop)

run()