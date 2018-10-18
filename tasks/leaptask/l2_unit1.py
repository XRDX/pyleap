from pyleap import *
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
	