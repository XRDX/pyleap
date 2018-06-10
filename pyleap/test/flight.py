from pyleap import *
import random

window.set_caption("雷霆战机")

bg = Sprite("../../images/bg.jpg")
bg.scale = 4

hero = Sprite("../../images/hero.png", 100, 100)
enemy = Sprite("../../images/enemy.png")
bullet = Sprite("../../images/bullet.png")


def draw():
    window.clear()
    bg.draw()
    hero.draw()
    enemy.draw()
    bullet.draw()


def new_enemy():
    enemy.x = random.randint(0, window.w)
    enemy.y = window.h


def main(dt):
    bullet.y += 50
    if bullet.y > window.h:
        bullet.x = hero.x
        bullet.y = hero.y

    enemy.y -= 2
    if enemy.y < 0 or bullet.collide(enemy):
        new_enemy()

    draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y


mouse.on_move(move)

schedule_interval(main, 1 / 60)
run()
