from pyleap import *

c = Circle(100, 200, 50, "red")

def update(dt):
    c.x += 1


def draw(dt):
    # update()
    window.clear()
    c.draw()
    window.show_fps()


def start_move():
    repeat(update, 1 / 60)

def stop_move():
    stop(update)


mouse.on_press(start_move)
mouse.on_release(stop_move)


repeat(draw, 1 / 60)
run()
