from pyleap import *
import random

bg = Rectangle(0, 0, window.w, window.h, "white")
c = Circle()
retry = Text("Try Again", font_size=30)
score = 0

def draw(dt):
    bg.draw()
    c.draw()
    Text(str(score), 10, window.h-20).draw()
    
    if(c.y < 0):
        stop(update)
        retry.draw()

def update(dt):
    c.y -= score

def new_c():
    global score
    score += 1
    c.color = hsla(random.randint(0, 360), a=0.5+random.random())
    c.r = random.randint(20, 40)
    c.y = window.h + c.r
    c.x = random.randint(c.r, window.w-c.r)

new_c()

def start():
    global score
    score = 0
    new_c()
    repeat(update)

c.on_press(new_c)
retry.on_press(start)

repeat(draw)

start()
run()
