from pyleap import *


hero = Sprite("https://rss.leaplearner.com/Image/Role/Fish6.png")
enemy = Sprite("https://rss.leaplearner.com/Image/Role/Fighter10.png")

hero.scale = 0.5
enemy.scale = 0.5

collide_circle = Circle(r=10)



def draw(dt):
    window.clear()
    p = hero.collide(enemy)
    hero.draw()
    enemy.draw()
    if(p):
        collide_circle.x = p[0]
        collide_circle.y = p[1]
        collide_circle.draw()


def move():
    hero.x = mouse.x
    hero.y = mouse.y

mouse.on_move(move)

schedule_interval(draw)

run()
