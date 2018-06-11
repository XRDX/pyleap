from pyleap import *

c = Circle(100, 200, 50, "red")

def update(dt):
    c.x += 1


def draw(dt):
    # update()
    window.clear()
    c.draw()


def start_move():
    schedule_interval(update, 1 / 60)

def stop_move():
    unschedule(update)


mouse.on_press(start_move)
mouse.on_release(stop_move)


schedule_interval(draw, 1 / 60)
run()
