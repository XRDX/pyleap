from pyleap import *
import random


def chase(self, hero):
    r = ((hero.x - self.x)**2 + (hero.y-self.y)**2)**0.5
    if(r<5):
        r = 5
    self.x += self.speed * (hero.x - self.x) / r
    self.y += self.speed * (hero.y - self.y) / r


Sprite.chase = chase
m_batch = Batch()

class Monster(Sprite):

    def __init__(self, x=0, y=0):
        src = "https://rss.leaplearner.com/Image/Role/CircleFace.png"
        super().__init__(src, x, y, 30, 30, batch=m_batch)
        self.speed = 0.5 + random.random() * 0.5


monsters = []


bg = Sprite("https://rss.leaplearner.com/Image/Bgs/BG.png")
hero = Sprite("https://rss.leaplearner.com/Image/Role/Alien2.png", w=100, h=100)
hero.src = "https://rss.leaplearner.com/Image/Role/CircleFace.png"
hero.speed = 5
hero.opacity = 0.5

t = Text("RETRY!", font_size=30)

def add_monster(dt):
    if(random.random() > 0.5):
        y = 0
    else:
        y = window.h
    
    m = Monster(random.randint(0, window.w), y)
    monsters.append(m)

def game(dt):
    window.clear()
    hero.chase(mouse)

    bg.draw()
    hero.draw()

    for m in monsters:
        m.chase(hero)
        #m.draw()

    m_batch.draw()

    for m in monsters:
        if(m.collide(hero)):
            t.draw()
            stop(game)
            break
    window.show_fps()

def retry():
    global monsters
    monsters = []
    repeat(game)
    
t.on_press(retry)

repeat(game)
repeat(add_monster, 1)
run()
