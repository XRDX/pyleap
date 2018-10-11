from pyleap import *

# 创建对象
title = Text("LeapLearner", 60, 380, 50)
mike = Sprite("https://rss.leaplearner.com/Image/Role/Frog1.png", 250, 240)

# 绘制函数
def draw(dt):
    title.draw()
    mike.draw()