from pyleap import *
import random

bg = Sprite("https://rss.leaplearner.com/Image/Bgs/BG.png")
hero = Sprite("https://rss.leaplearner.com/Image/Role/Fighter15.png")
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png")
bullet = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")
msc = Audio("https://rss.leaplearner.com/Audio/BallGame/buySuccess.mp3")

bg.scale = 0.4
hero.scale = 0.8
enemy.scale = 0.5
bullet.scale = 0.1


def new_enemy():
    enemy.x = random.randint(0, window.w)
    enemy.y = window.h


def update(dt):
    bullet.y += 10
    if bullet.y > window.h:
        bullet.x = hero.x
        bullet.y = hero.y

    enemy.y -= 2
    if enemy.y < 0 or bullet.collide(enemy):
        new_enemy()


def draw(dt):
    window.clear()
    bg.draw()
    hero.draw()
    enemy.draw()
    bullet.draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.on_move(move)
mouse.on_press(msc.play)

schedule_interval(update)
schedule_interval(draw)

run()
