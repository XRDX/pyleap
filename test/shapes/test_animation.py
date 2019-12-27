from pyleap import *

ani1 = Sprite("https://r.leaplearner.com/ud/production/A01T0018/udnt.gif")
ani2 = Sprite("https://r.leaplearner.com/ud/production/958096/QcMd.gif", 200, 200, 100, 100)
ani2.set_anchor(250, 250)

def draw(dt):
	window.clear()
	ani1.draw()
	ani2.rotation += 1
	ani2.draw()

repeat(draw)
run()