from pyleap import *

window.set_size(900,600)
# 创建对象
bg = Sprite("https://r.leaplearner.com/ud/production/207155/ZoWs.jpg", 450,400)
bg.scale = 1.8
def star(x,y):
    star = Sprite("https://r.leaplearner.com/ud/production/615020/4dks.png",x,y)
    star.scale = 0.15
    star.draw()
def star2(x, y):
    star2 = Sprite("https://r.leaplearner.com/ud/production/615020/NeHP.png",x,y)
    star2.scale = 0.15
    star2.draw()
def draw1():    
    bg.draw()
    window.show_axis()

