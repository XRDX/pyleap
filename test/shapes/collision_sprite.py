from pyleap import *
from pyglet.gl import *


hero = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png", 300, 300, 100, 100)
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png", 300, 300, 100, 100)

p = Point(point_size=10)

def draw(dt):
    window.clear()
    window.show_axis()
    enemy.rotation += 1
    c = hero.collide(enemy)
    hero.draw()
    enemy.draw()
    if(c):
        p.x = c.x
        p.y = c.y
        p.draw()
    window.show_fps()

def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.on_move(move)

repeat(draw)

run()
