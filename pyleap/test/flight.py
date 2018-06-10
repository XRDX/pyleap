from pyleap import *
import random

canvas.set_caption("雷霆战机")

bg = Sprite("../../images/bg.jpg")
bg.scale = 4

hero = Sprite("../../images/hero.png", 100, 100)
enemy = Sprite("../../images/enemy.png")
bullet = Sprite("../../images/bullet.png")


def draw():
    canvas.clear()
    bg.draw()
    hero.draw()
    enemy.draw()
    bullet.draw()


def new_enemy():
    enemy.x = random.randint(0, canvas.w)
    enemy.y = canvas.h


def main(dt):
    bullet.y += 500 * dt
    if bullet.y > canvas.h:
        bullet.x = hero.x
        bullet.y = hero.y

    enemy.y -= 100 * dt
    if enemy.y < 0 or bullet.collide(enemy):
        new_enemy()

    draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y


mouse.move = move

setInterval(main, 1 / 60)
run()
