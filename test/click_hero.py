from pyleap import *
import random

bg = Rectangle(0, 0, window.w, window.h, "white")
c = Circle()
retry = Text("Try Again")

def draw(dt):
    bg.draw()
    c.draw()
    if(c.y < 0):
        stop(update)
        retry.draw()

def update(dt):
    c.y -= 1

def new_c():
    c.color = hsl(random.randint(0, 360))
    c.y = window.h + c.r
    c.x = random.randint(c.r, window.w-c.r)

new_c()

def start():
    new_c()
    repeat(update)

c.on_press(new_c)
retry.on_press(start)

repeat(draw)

start()
run()