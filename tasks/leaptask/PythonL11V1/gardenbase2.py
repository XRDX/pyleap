from pyleap import *
#from garden import *
import random
import math

#云
def draw_cloud(cloud_number=0):
    #从左到右
    if cloud_number == 1:
        #云朵1
        Ellipse(90, 70, 60, 28, 'white').draw()
        Ellipse(43, 67, 50, 20, 'white').draw()
        Ellipse(150, 70, 30, 20, 'white').draw()    
    elif cloud_number == 2:
        #云朵1
        Ellipse(90, 70, 60, 28, 'white').draw()
        Ellipse(43, 67, 50, 20, 'white').draw()
        Ellipse(150, 70, 30, 20, 'white').draw()
        #云朵2
        Ellipse(320, 50, 60, 28, 'white').draw()
        Ellipse(370, 50, 30, 20, 'white').draw()
    elif cloud_number == 3:
        #云朵1
        Ellipse(90, 70, 60, 28, 'white').draw()
        Ellipse(43, 67, 50, 20, 'white').draw()
        Ellipse(150, 70, 30, 20, 'white').draw()
        #云朵2
        Ellipse(320, 50, 60, 28, 'white').draw()
        Ellipse(370, 50, 30, 20, 'white').draw()
        #云朵3
        Ellipse(490, 110, 60, 28, 'white').draw()
        Ellipse(545, 100, 50, 20, 'white').draw()
    elif cloud_number == 4:
        #云朵1
        Ellipse(90, 70, 60, 28, 'white').draw()
        Ellipse(43, 67, 50, 20, 'white').draw()
        Ellipse(150, 70, 30, 20, 'white').draw()
        #云朵2
        Ellipse(320, 50, 60, 28, 'white').draw()
        Ellipse(370, 50, 30, 20, 'white').draw()
        #云朵3
        Ellipse(490, 110, 60, 28, 'white').draw()
        Ellipse(545, 100, 50, 20, 'white').draw()
        #云朵4
        Ellipse(500, 40, 60, 20, 'white').draw()
def draw_flower(flower_number=0):
    if flower_number == 1:
        flower1 = Sprite("https://r.leaplearner.com/ud/production/615020/uIcq.png", 50, 170)
        flower1.scale = 0.2
        flower1.draw()
    elif flower_number == 2:
        flower1 = Sprite("https://r.leaplearner.com/ud/production/615020/uIcq.png", 50, 170)
        flower2 = Sprite("https://r.leaplearner.com/ud/production/615020/s4P3.png", 80, 200)
        flower1.scale = 0.2
        flower2.scale = 0.2
        flower1.draw()
        flower2.draw()
    elif flower_number == 3:
        flower1 = Sprite("https://r.leaplearner.com/ud/production/615020/uIcq.png", 50, 170)
        flower2 = Sprite("https://r.leaplearner.com/ud/production/615020/s4P3.png", 80, 200)
        flower3 = Sprite("https://r.leaplearner.com/ud/production/615020/RBTJ.png", 110, 220)
        flower1.scale = 0.2
        flower2.scale = 0.2
        flower3.scale = 0.2
        flower1.draw()
        flower2.draw()
        flower3.draw()
    elif flower_number == 4:
        flower1 = Sprite("https://r.leaplearner.com/ud/production/615020/uIcq.png", 50, 170)
        flower2 = Sprite("https://r.leaplearner.com/ud/production/615020/s4P3.png", 80, 200)
        flower3 = Sprite("https://r.leaplearner.com/ud/production/615020/RBTJ.png", 110, 220)
        flower4 = Sprite("https://r.leaplearner.com/ud/production/615020/HeqZ.png", 160, 280)
        flower1.scale = 0.2
        flower2.scale = 0.2
        flower3.scale = 0.2
        flower4.scale = 0.2
        flower1.draw()
        flower2.draw()
        flower3.draw()
        flower4.draw()

#树n
t1 = Ellipse(345, 300, 20, 30, "black")
t2 = Ellipse(380, 290, 15, 35, "black")
t3 = Ellipse(400, 320, 20, 40, "black")
t4 = Ellipse(385, 150, 20, 30, "black")
t5 = Ellipse(435, 170, 20, 40, "black")
t6 = Ellipse(500, 280, 20, 40, "black")
t7 = Ellipse(530, 320, 20, 40, "black")
t8 = Ellipse(555, 250, 20, 40, "black")
t9 = Ellipse(590, 275, 15, 30, "black")
t10 = Ellipse(610, 320, 15, 45, "black")
#飞机
plane = Sprite("https://r.leaplearner.com/ud/production/615020/zes9.png", 500, 400)

#鱼
fish1 = Sprite("https://r.leaplearner.com/ud/production/615020/FnX7.png", 156, 127)
fish2 = Sprite("https://r.leaplearner.com/ud/production/615020/jeu6.png", 16, 129)
fish3 = Sprite("https://r.leaplearner.com/ud/production/615020/Gd98.png", 160, 156)
#天空
skys = Rectangle(0, 0, 650, 500, "blue")
#太阳和月亮
suns = Circle(100, 420, 50, "orange")
def draw_all(dt):
    window.set_size(650, 500)
    #背景天空
    skys.draw()
        
    #太阳    
    suns.draw()

    #空中花园基地
    Ellipse(325, 200, 500, 100, '#CCCC33').draw()

    #河流
    river = '#66CCFF'
    Rectangle(0, 0, 32, 148, river).draw()
    Rectangle(32, 116, 150, 32, river).draw()
    Rectangle(130, 136, 400, 32, river).draw()
    if showfish == True:
        #鱼
        fish2.scale = 0.09
        fish1.scale = 0.08
        fish3.scale = 0.08
        fish1.draw()
        fish2.draw()
        fish3.draw() 
 
    #山丘
    Triangle(460, 300, 360, 170, 650, 170, '#CCCC99').draw()
    Triangle(450, 105, 580, 255, 700, 120, '#9999CC').draw()
    #亭子
    Triangle(370, 250, 340, 220, 400, 220, '#996633').draw()
    Rectangle(345, 185, 5, 35, '#663300').draw()
    Rectangle(390, 185, 5, 35, '#663300').draw()
    Line(340,185,400,185,3,'#333333').draw()

    #大树
    #左上三棵树
    #树1
    t1.draw()
    Line(345, 290, 345, 250, 2, '#663300').draw()
    #树2
    t2.draw()
    Line(380, 290, 380, 245, 2, '#663300').draw()
    #树3
    t3.draw()
    Line(400, 320, 400, 260, 2, '#663300').draw()

    #左下两棵
    #树4
    t4.draw()
    Line(385, 150, 385, 100, 2, '#663300').draw()
    #树5
    t5.draw()
    Line(435, 170, 435, 100, 2, '#663300').draw()
    
    #右上五棵树
    #树6
    t6.draw()
    Line(500, 280, 500, 230, 2, '#663300').draw()
    #树7
    t7.draw()
    Line(530, 320, 530, 270, 2, '#663300').draw()
    #树8
    t8.draw()
    Line(555, 250, 555, 205, 2, '#663300').draw()
    #树9
    t9.draw()
    Line(590, 275, 590, 234, 2, '#663300').draw()
    #树10
    t10.draw()
    Line(610, 260, 610, 320,  2, '#663300').draw()
               
    #云
    draw_cloud(cloud_number)

    #花
    draw_flower(flower_number)
    
    #飞机
    plane.scale = 0.5
    plane.draw()
    window.show_axis()
    
def s(x=500, y=400, flower=0, cloud=0, tree1="black", tree2="black", tree3="black", tree4="black", tree5="black", tree6="black",
      tree7="black", tree8="black", tree9="black", tree10="black", speed1=0, speed2=0, speed3=0):
    global showfish,flower_number,cloud_number,planex,planey
    planex = x
    planey = y
    showfish = True
    flower_number = flower
    cloud_number = cloud
    t1.color = tree1
    t2.color = tree2
    t3.color = tree3
    t4.color = tree4
    t5.color = tree5
    t6.color = tree6
    t7.color = tree7
    t8.color = tree8
    t9.color = tree9
    t10.color = tree10
    #speed = speed
    speed1 = speed1
    speed2 = speed2
    speed3 = speed3
    def swiming(dt):
        fish1.x -= speed1
        fish2.y -= speed2
        fish3.x += speed3
    def fly(dt):
        dx = planex - plane.x
        dy = planey - plane.y
        ds = math.sqrt(dx**2 + dy**2)
        if planex > plane.x and dx > 0: 
            plane.x = plane.x + dx / ds
        elif planex < plane.x and dx < 0:
            plane.x = plane.x + dx / ds
        if planey > plane.y and dy > 0: 
            plane.y = plane.y + dy / ds
        elif planey < plane.y and dy < 0: 
            plane.y = plane.y + dy / ds
        
    repeat(draw_all)
    repeat(fly)
    repeat(swiming)
    run()
    
