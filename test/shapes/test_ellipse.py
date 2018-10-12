from pyleap import *

elli = Ellipse(200, 200, 140, 60, "red")

def draw(dt):
    window.clear()
    elli.rotation += 1
    elli.draw()

repeat(draw)
run()