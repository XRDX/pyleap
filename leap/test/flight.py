import sys
sys.path.append('../')
sys.path.append('../src')

from src import *

canvas.set_caption("雷霆战机")

bg = Sprite("../images/bg.jpg", canvas.width // 2, canvas.height // 2)
bg.scale_x = canvas.width / bg.img.width
bg.scale_y = canvas.height / bg.img.height

hero = Sprite("../images/hero.png", 100, 100)


def update(dt):
    canvas.clear()
    bg.draw()
    hero.draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.move = move

setInterval(update, 1 / 60)
run()
