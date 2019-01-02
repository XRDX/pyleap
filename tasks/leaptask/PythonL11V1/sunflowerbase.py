from pyleap import *
window.set_size(600,600)


c1 = Circle(300,300,160)
e1 = Ellipse(300,80,27,70)
def draw(dt):
    sky = Sprite("https://r.leaplearner.com/ud/production/615020/kw2Y.png", 0, 0)
    sky.scale = 3
    sky.draw()
    a = 0    
    e1.set_anchor(300,300)
    for i in range(n):
        a = a + 15
        e1.rotation = a
        e1.draw()
    c1.draw()
    Line(195,180,405,180,3,'black').draw()
    Line(162,220,437,220,3,'black').draw()
    Line(145,260,455,260,3,'black').draw()
    Line(140,300,460,300,3,'black').draw()
    Line(145,340,455,340,3,'black').draw()
    Line(162,380,437,380,3,'black').draw()
    Line(195,420,405,420,3,'black').draw()
    Line(180,195,180,405,3,'black').draw()
    Line(220,162,220,437,3,'black').draw()
    Line(260,145,260,455,3,'black').draw()
    Line(300,140,300,460,3,'black').draw()
    Line(340,145,340,455,3,'black').draw()
    Line(380,162,380,437,3,'black').draw()
    Line(420,195,420,405,3,'black').draw()
def get(number=1, color1="white", color2="black"):
    global n
    n = number
    c1.color = color1
    e1.color = color2
    repeat(draw)
    run()

