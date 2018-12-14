from pyleap import *


hero = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")

hero.scale_y = 0.5
hero.scale_x = 0.5
hero.scale = 1


def draw(dt):
    window.clear()
    hero.h += 1
    hero.draw()


repeat(draw)
run()
