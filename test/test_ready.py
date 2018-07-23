from pyleap import *

bg = Sprite("https://rss.leaplearner.com/Image/Bgs/BG.png")

@window.event
def on_expose():
    bg.draw()


run()