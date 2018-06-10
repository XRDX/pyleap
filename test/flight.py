from pyleap import *
import random

window.set_caption("雷霆战机")

bg = Sprite("https://rss.leaplearner.com/Image/Bgs/BG.png")
bg.scale = 0.4
hero = Sprite("https://rss.leaplearner.com/Image/Role/Fighter15.png", 100, 100)
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png")
bullet = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")
bullet.scale = 0.2
# msc = Audio("../../images/foodback.mp3")


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
# mouse.on_press(msc.play)

schedule_interval(main, 1 / 60)
run()
