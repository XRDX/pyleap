from pyleap import *
from pyglet import gl
import math, random
targets = []
# Lesson 1
spaceship = Sprite("https://r.leaplearner.com/i/Fighter15.png", 50, 50)
spaceship.scale = 0.4
target = {'x': -100, 'y':-100}
rain = []
for i in range(0, 50):
	rain.append(Sprite("https://r.leaplearner.com/ud/production/A01T0008/EpZi.png", random.randint(0, 800), random.randint(500, 1000)))

def detect(x, y):
	global target
	target['x'] = x
	target['y'] = y

def space1():
	global spaceship, targets
	window.set_size(800, 400)
	window.clear()
	txt = Text("用fly_to(x坐标, y坐标)来控制飞船飞行吧！", 100, 350, 15, "white")
	space = Sprite("https://r.leaplearner.com/ud/production/A01T0008/o9hm.jpg", 400, 200)
	space.draw()
	window.show_axis()
	spaceship.draw()
	if (len(targets) > 0):
		dx = targets[0]['x'] - spaceship.x
		dy = targets[0]['y'] - spaceship.y
		ds = math.sqrt(dx*dx + dy*dy)
		if (ds < 150):
			spaceship.set_anchor(spaceship.x, spaceship.y)
			if (dy == 0):
				if (dx > 0):
					spaceship.rotation = 270
				elif (dx < 0):
					spaceship.rotation = 90
			elif (dy < 0):
				spaceship.rotation = 180 + math.degrees(math.atan(-dx/dy))
			else:
				spaceship.rotation = math.degrees(math.atan(-dx/dy))
			if (ds < 5):
				spaceship.x = targets[0]['x']
				spaceship.y = targets[0]['y']
				if (len(targets) > 1):
					targets.pop(0)
				txt.src = "到达目的地：(" + str(targets[0]['x']) + ", " + str(targets[0]['y']) + ")"
			else:
				spaceship.x = spaceship.x + dx / ds
				spaceship.y = spaceship.y + dy / ds
				txt.src = "正在飞往：(" + str(targets[0]['x']) + ", " + str(targets[0]['y']) + ")"
		else:
			txt.src = "飞行距离过长，请降落到更近的星球"
	txt.draw()
def fly_to(x, y):
	global targets
	targets.append({'x': x, 'y':y})

def space2():
	global target, rain
	window.set_size(800, 500)
	window.clear()
	robot = Sprite("https://r.leaplearner.com/i/robot_3.png", target['x'], target['y'] + 30)
	arrow = Sprite("https://r.leaplearner.com/ud/production/A01T0008/9WZr.png", target['x'], target['y'])
	# arrow = Triangle(target['x'], target['y'] + 10, target['x']-7, target['y'] - 10, target['x']+7, target['y'] - 10, "red")
	txt = Text("用detect命令控制小乐探测水源吧！", 140, 450, 25, "black")
	water = Sprite("https://r.leaplearner.com/ud/production/A01T0008/EpZi.png", 535, 250)
	bg = Sprite("https://r.leaplearner.com/ud/production/A01T0008/uH1W.jpg", 300, 250)
	water.scale = 0.7
	robot.scale = 0.6
	bg.scale = 1.8
	arrow.scale = 0.35
	bg.draw()
	window.show_axis()
	robot.draw()
	dx = water.x - target['x']
	dy = water.y - target['y']
	ds = math.sqrt(dx*dx+dy*dy)
	if (target['x'] >= 0 and target['y'] >= 0):
		if (ds < 25):
			txt.src = "哇！我们找到了水源！太棒啦！"
			txt.x = 100
			for drop in rain:
				drop.y = drop.y - 10
				if (drop.y < 0):
					drop.y = 550
					drop.x = random.randint(0, 800)
				drop.scale = 0.5
				drop.draw()
		else:
			if (ds < 150):
				txt.src = "水源应该就在不远处……"
				txt.x = 140
				# arrow.color = "green"
			elif (ds < 300):
				txt.src = "emmm，我们离水源应该还有一些距离"
				txt.x = 60
				# arrow.color = "orange"
			else:
				txt.src = "再找找吧，这里根本没有水源的迹象"
				txt.x = 70
				# arrow.color = "red"
			if (dy == 0):
				arrow.set_anchor(target['x'], target['y'])
				if (dx > 0):
					arrow.rotation = 270 + random.randint(-5,6)
				else:
					arrow.rotation = 90 + random.randint(-5,6)
				arrow.draw()
			elif (dy<0):
				arrow.set_anchor(target['x'], target['y'])
				arrow.rotation = 180 + math.degrees(math.atan(-dx/dy)) + random.randint(-5,6)
				arrow.draw()
			else:
				arrow.set_anchor(target['x'], target['y'])
				arrow.rotation = math.degrees(math.atan(-dx/dy)) + random.randint(-5,6)
				arrow.draw()
	txt.draw()
def sky():
	_star = Sprite("https://r.leaplearner.com/ud/production/687283/BwjM.jpg", 250, 250)
	window.set_size(500, 500)
	_star.draw()
	window.show_axis()

def astro():
	_star = Sprite("https://r.leaplearner.com/ud/production/687283/dJAT.jpg", 500, 500)
	window.set_size(1000, 1000)
	_star.draw()
	window.show_axis()

def star(x, y):
    _star = Circle(x, y, 5)
    _star.draw()



# Lesson 2
lines = []
ps = [[66, 88, 96, 134], [129, 169, 213, 196], [275, 204, 355, 187], [410, 171, 487, 132], [546, 139, 610, 195], [655, 237, 698, 293]]
class Line(Shape):
	def __init__(self, x1=100, y1=100, x2=200, y2=200, line_width=1, color="orange"):
		""" 线段
		线段宽度： line_width， 默认为1
		颜色： color, 默认为"orange"
		"""
		x = (x1 + x2) / 2
		y = (y1 + y2) / 2
		super().__init__(x, y, color, gl=gl.GL_LINES, line_width=line_width)
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		lines.append(self)

	def update_points(self):
		self.points = (self.x1, self.y1, self.x2, self.y2)	

def check(self, x1, y1, x2, y2, ds):
	dx1 = self.x1 - x1
	dy1 = self.y1 - y1
	dx2 = self.x2 - x2
	dy2 = self.y2 - y2
	ds1 = math.sqrt(dx1*dx1+dy1*dy1)
	ds2 = math.sqrt(dx2*dx2+dy2*dy2)
	if (ds1<=ds and ds2<= ds):
		return True
	else:
		return False

Line.check = check
def space3():
	global spaceship, targets, lines
	window.set_size(800, 400)
	window.clear()
	txt = Text("为地球上的人们搭建星际廊桥吧！", 100, 350, 15, "white")
	space = Sprite("https://r.leaplearner.com/ud/production/A01T0008/nUuI.jpg", 400, 200)
	space.draw()
	window.show_axis()
	bridge_amt = 0
	for i in range(len(lines)):
		if (lines[i].check(ps[i][0], ps[i][1], ps[i][2], ps[i][3], 5) or lines[i].check(ps[i][2], ps[i][3], ps[i][0], ps[i][1], 5)):
			bridge_amt = bridge_amt + 1
			txt.src = "已经搭建完成" + str(bridge_amt) + "条星际廊桥"
		else:
			lines[i].x1 += random.randint(-1, 1)
			lines[i].y1 += random.randint(0, 2)
			lines[i].x2 += random.randint(-1, 1)
			lines[i].y2 += random.randint(0, 2)
	txt.draw()

def shape_q1():
	window.set_size(700, 800)
	bg = Rectangle(0, 0, 700, 800, "white")
	bg.draw()
	window.show_axis()
	lines = []

	lines.append(Line(100, 600, 200, 500, 2, "red"))
	lines.append(Line(300, 600, 400, 500, 6, "green"))
	lines.append(Line(500, 600, 600, 500, 10, "blue"))
	lines.append(Line(100, 400, 200, 300, 2, "green"))
	lines.append(Line(300, 400, 400, 300, 10, "blue"))
	lines.append(Line(500, 400, 600, 300, 6, "red"))
	lines.append(Line(100, 200, 200, 100, 6, "green"))
	lines.append(Line(300, 200, 400, 100, 10, "red"))

	lines.append(Line(150, 600, 150, 550, 6, "black"))
	lines.append(Line(350, 550, 400, 550, 6, "black"))
	lines.append(Line(550, 550, 550, 500, 6, "black"))
	lines.append(Line(150, 350, 100, 350, 6, "black"))
	lines.append(Line(350, 400, 350, 350, 6, "black"))
	lines.append(Line(550, 350, 600, 350, 6, "black"))
	lines.append(Line(150, 150, 150, 100, 6, "black"))
	lines.append(Line(350, 150, 300, 150, 6, "black"))

	lines.append(Rectangle(500, 100, 100, 100, "#EEEEEE"))
	lines.append(Text("?", 525, 120, 60, "white"))
	lines.append(Text("找规律，画出最后一个图形", 100, 700, 28, "black"))

	for l in lines:
		l.draw()

def shape_q2():
	window.set_size(700, 800)
	bg = Rectangle(0, 0, 700, 800, "white")
	bg.draw()
	window.show_axis()
	lines = []
	lines.append(Line(100, 600, 200, 600, 5, "blue"))
	lines.append(Line(100, 550, 200, 550, 10, "green"))
	lines.append(Line(100, 500, 200, 500, 15, "red"))
	lines.append(Line(300, 600, 300, 500, 5, "blue"))
	lines.append(Line(350, 600, 350, 500, 10, "green"))
	lines.append(Line(400, 600, 400, 500, 15, "red"))
	lines.append(Line(500, 600, 600, 600, 15, "red"))
	lines.append(Line(500, 550, 600, 550, 10, "green"))
	lines.append(Line(500, 500, 600, 500, 5, "blue"))

	lines.append(Line(100, 400, 100, 300, 5, "red"))
	lines.append(Line(150, 400, 150, 300, 10, "blue"))
	lines.append(Line(200, 400, 200, 300, 15, "green"))
	lines.append(Line(300, 400, 400, 400, 15, "green"))
	lines.append(Line(300, 350, 400, 350, 10, "blue"))
	lines.append(Line(300, 300, 400, 300, 5, "red"))
	lines.append(Line(500, 400, 500, 300, 15, "green"))
	lines.append(Line(550, 400, 550, 300, 10, "blue"))
	lines.append(Line(600, 400, 600, 300, 5, "red"))
	
	lines.append(Line(100, 200, 200, 200, 5, "green"))
	lines.append(Line(100, 150, 200, 150, 10, "red"))
	lines.append(Line(100, 100, 200, 100, 15, "blue"))
	lines.append(Line(300, 200, 300, 100, 5, "green"))
	lines.append(Line(350, 200, 350, 100, 10, "red"))
	lines.append(Line(400, 200, 400, 100, 15, "blue"))

	lines.append(Rectangle(500, 100, 100, 100, "#EEEEEE"))
	lines.append(Text("?", 525, 120, 60, "white"))
	lines.append(Text("找规律，画出最后一个图形", 100, 700, 28, "black"))

	for l in lines:
		l.draw()

def shape_q3():
	window.set_size(600, 700)
	bg = Rectangle(0, 0, 600, 700, "white")
	bg.draw()
	window.show_axis()
	lines = []
	lines.append(Text("用四条相连的线段连接所有圆点", 100, 550, 20, "black"))
	for i in range(0, 9):
		lines.append(Circle(200 + 100 * (i % 3), 200 + 100 * (i - i % 3) / 3, 10, "black"))
	for l in lines:
		l.draw()

def shape_q4():
	window.set_size(800, 800)
	bg = Rectangle(0, 0, 800, 800, "white")
	bg.draw()
	window.show_axis()
	lines = []
	t = Text("请画出四条线段，分别将下列图形分成面积相等的两部分", 100, 700, 15, "black")
	t.draw()
	lines.append(Circle(200, 200, 100))
	lines.append(Polygon(100, 600, 250, 600, 300, 400, 150, 400))
	lines.append(Triangle(450, 600, 700, 400, 400, 400))
	lines.append(Rectangle(400, 100, 300, 200))
	for l in lines:
		l.color = "blue"
		l.line_width = 3
		l.stroke()

# Lesson 3
def emoji1():
	window.set_size(400, 400)
	bg = Rectangle(0, 0, 400, 400, "white")
	bg.draw()
	face = Circle(200, 200, 150, "gray")
	face.stroke()
	mouth = Rectangle(150, 125, 100, 10, "gray")
	mouth.stroke()
	left_eye = Circle(150, 230, 15, "gray")
	left_eye.stroke()
	right_eye = Circle(250, 230, 15, "gray")
	right_eye.stroke()

def emoji2():
	window.set_size(400, 400)
	bg = Rectangle(0, 0, 400, 400, "white")
	bg.draw()
	face = Circle(200, 200, 150, "gray")
	face.stroke()
	mouth = Rectangle(170, 125, 60, 10, "gray")
	mouth.stroke()
	left_eyebrow = Line(160, 305, 105, 285, 10, "gray")
	left_eyebrow.stroke()
	left_eyebrow1 = Line(159, 304.6, 106, 285.3, 8, "white")
	left_eyebrow1.draw()
	right_eyebrow = Line(240, 305, 295, 285, 10, "gray")
	right_eyebrow.stroke()
	right_eyebrow1 = Line(241, 304.6, 294, 285.3, 8, "white")
	right_eyebrow1.draw()
	left_eye = Circle(140, 220, 40, "gray")
	left_eye.stroke()
	left_eye1 = Circle(140, 220, 10, "gray")
	left_eye1.stroke()
	right_eye = Circle(260, 220, 40, "gray")
	right_eye.stroke()
	right_eye1 = Circle(260, 220, 10, "gray")
	right_eye1.stroke()

def emoji3():
	window.set_size(400, 400)
	bg = Rectangle(0, 0, 400, 400, "white")
	bg.draw()
	face = Circle(200, 200, 150, "gray")
	face.stroke()
	mouth = Rectangle(170, 125, 60, 10, "gray")
	mouth.stroke()
	left_eyebrow = Line(160, 305, 105, 285, 10, "gray")
	left_eyebrow.stroke()
	left_eyebrow1 = Line(159, 304.6, 106, 285.3, 8, "white")
	left_eyebrow1.draw()
	right_eyebrow = Line(240, 305, 295, 285, 10, "gray")
	right_eyebrow.stroke()
	right_eyebrow1 = Line(241, 304.6, 294, 285.3, 8, "white")
	right_eyebrow1.draw()
	left_eye = Circle(140, 220, 40, "gray")
	left_eye.stroke()
	left_eye1 = Circle(140, 220, 10, "gray")
	left_eye1.stroke()
	right_eye = Circle(260, 220, 40, "gray")
	right_eye.stroke()
	right_eye1 = Circle(260, 220, 10, "gray")
	right_eye1.stroke()
	
def mars_rover1():
    window.set_size(800, 600)
    a = [];
    a.append(Rectangle(0, 0, 800, 600, "#FFF8DC"))
    n = Sprite("https://r.leaplearner.com/ud/production/A01T0008/vOmW.png", 400, 300)
    n.scale = 0.6
    a.append(n)
    a.append(Rectangle(458, 280, 24, 132, "black"))
    a.append(Rectangle(460, 280, 20, 130, "#DDDDDD"))
    a.append(Rectangle(298, 198, 204, 104, "black"))
    a.append(Rectangle(220, 305, 20, 20, "orange"))
    a.append(Rectangle(222, 325, 16, 70, "black"))
    a.append(Rectangle(224, 325, 12, 68, "red"))
    a.append(Rectangle(300, 200, 200, 100, "#DDDDDD"))
    a.append(Rectangle(198, 298, 304, 14, "black"))
    a.append(Rectangle(200, 300, 300, 10, "#DDDDDD"))
    a.append(Rectangle(428, 398, 84, 34, "black"))
    a.append(Rectangle(430, 400, 80, 30, "#DDDDDD"))
    a.append(Polygon(290, 340, 280, 310, 300, 310, "black"))
    a.append(Circle(290, 340, 10, "orange"))
    a.append(Polygon(268, 425, 275, 360, 310, 325, 375, 313, "#DDDDDD"))
    n = Ellipse(325, 370, 18, 78, "orange")
    n.set_anchor(325, 370)
    n.rotation = 45
    a.append(n)
    n = Ellipse(320, 370, 10, 55, "white")
    n.set_anchor(325, 370)
    n.rotation = 45
    a.append(n)
    n = Rectangle(310, 365, 15, 10, "black")
    n.set_anchor(325, 370)
    n.rotation = 45
    a.append(n)
    a.append(Line(500, 300, 550, 400, 20, "orange"))
    a.append(Line(550, 400, 665, 380, 20, "orange"))
    a.append(Polygon(660, 370, 680, 350, 730, 350, 730, 355, 685, 365, 675, 385, "black"))
    a.append(Polygon(690, 402, 730, 410, 729, 416, 680, 415, 655, 385, 675, 385, "black"))
    a.append(Circle(550, 400, 12, "black"))
    a.append(Circle(550, 400, 10, "white"))
    a.append(Circle(550, 400, 5, "black"))
    a.append(Circle(665, 380, 12, "black"))
    a.append(Circle(665, 380, 10, "white"))
    a.append(Circle(665, 380, 5, "black"))
    a.append(Circle(500, 300, 12, "black"))
    a.append(Circle(500, 300, 10, "white"))
    a.append(Circle(500, 300, 5, "black"))
    a.append(Circle(450, 425, 17, "black"))
    a.append(Circle(450, 425, 15, "orange"))
    a.append(Circle(450, 425, 12, "white"))
    a.append(Circle(490, 425, 17, "black"))
    a.append(Circle(490, 425, 15, "orange"))
    a.append(Circle(490, 425, 12, "white"))
    a.append(Circle(490, 425, 11, "blue"))
    a.append(Circle(150, 140, 50, "black"))
    a.append(Circle(150, 140, 40, "gray"))
    a.append(Circle(150, 140, 10, "orange"))
    a.append(Circle(390, 140, 50, "black"))
    a.append(Circle(390, 140, 40, "gray"))
    a.append(Circle(390, 140, 10, "orange"))
    a.append(Circle(660, 140, 50, "white"))
    a.append(Line(310, 280, 560, 280, 20, "orange"))
    a.append(Line(310, 280, 260, 210, 20, "orange"))
    a.append(Circle(310, 280, 10, "orange"))
    a.append(Line(200, 210, 340, 210, 20, "orange"))
    a.append(Line(200, 210, 150, 140, 20, "orange"))
    a.append(Line(340, 210, 390, 140, 20, "orange"))
    a.append(Circle(200, 210, 10, "orange"))
    a.append(Circle(340, 210, 10, "orange"))
    a.append(Circle(400, 280, 17, "black"))
    a.append(Circle(400, 280, 15, "white"))
    a.append(Circle(400, 280, 7, "black"))
    a.append(Circle(260, 210, 17, "white"))
    a.append(Circle(150, 140, 6, "black"))
    a.append(Circle(390, 140, 6, "black"))
    for shape in a:
        shape.draw()
        
def mars_rover2():  
    a = [];
    a.append(Line(560, 280, 660, 140, 20, "orange"))
    a.append(Circle(560, 280, 10, "orange"))
    a.append(Circle(660, 140, 10, "orange"))
    a.append(Circle(660, 140, 6, "black"))
    for shape in a:
        shape.draw()
    window.show_axis()

sate = Sprite("https://r.leaplearner.com/ud/production/A01T0008/bOGM.png", 300, 850)
sate.scale = 0.3
sate.set_anchor(300, 300)
angle = 0;
red_s = Sprite("https://r.leaplearner.com/ud/production/A01T0008/6kC3.png", 300, 300)
red_s.show = True
blue_s = Sprite("https://r.leaplearner.com/ud/production/A01T0008/X2ky.png", 300, 300)
blue_s.show = True
green_s = Sprite("https://r.leaplearner.com/ud/production/A01T0008/Rsi1.png", 300, 300)
green_s.show = True

def satellite():
    global angle
    window.set_size(600, 600)
    window.clear()
    bg = Sprite("https://r.leaplearner.com/ud/production/A01T0008/ezTx.jpg", 300, 300)
    bg.draw()
    window.show_axis()
    if (red_s.show):
        red_s.draw()
    if (blue_s.show):
        blue_s.draw()
    if (green_s.show):
        green_s.draw()
    angle -= 0.3

def launch(track):
    if (isinstance (track, Circle)):
        if (track.x == 300 and track.y == 300 and track.r > 160 and track.r < 180 and track.color == "red"):
            sate.x = 300
            sate.y = 850
            sate.rotation = angle
            sate.draw()
            red_s.show = False
        elif (track.x == 300 and track.y == 300 and track.r > 205 and track.r < 225 and track.color == "blue"):
            sate.x = 300
            sate.y = 1000
            sate.rotation = angle - 120
            sate.draw()
            blue_s.show = False
        elif (track.x == 300 and track.y == 300 and track.r > 246 and track.r < 266 and track.color == "green"):
            sate.x = 300
            sate.y = 1150
            sate.rotation = angle - 240
            sate.draw()
            green_s.show = False
            
def solar():
    window.set_size(800, 500)
    window.clear()
    bg = Sprite("https://r.leaplearner.com/ud/production/A01T0008/heEu.jpg", 400, 250)
    bg.draw()
    window.show_axis()