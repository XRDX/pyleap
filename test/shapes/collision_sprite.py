from pyleap import *
from pyglet.gl import *


hero = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png")

hero.scale_y = 0.5
hero.scale_x = 0.5
hero.scale = 0.5
# enemy.scale = 0.5

p = Point(point_size=10)


def draw(dt):
    window.clear()
    enemy.rotation += 1
    c = hero.collide(enemy)
    hero.draw()
    enemy.draw()
    if(c):
        p.x = c.x
        p.y = c.y
        p.draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.on_move(move)

repeat(draw)

run()
