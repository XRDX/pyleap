from pyleap import *
from pyglet.gl import *


hero = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png")

hero.scale = 0.5
enemy.scale = 0.5

p = Point(point_size=10)


def draw(dt):
    window.clear()
    c = hero.collide(enemy)
    hero.draw()
    enemy.draw()
    if(c):
        p.x = c[0]
        p.y = c[1]
        p.draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.on_move(move)

schedule_interval(draw)

run()
