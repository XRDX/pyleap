from pyleap import *
window.set_size(500, 500)
a1 = Circle(125,250,25,'white')
a2 = Circle(105,250,20,'white')
a3 = Circle(140,250,20,'white')
a4 = Circle(160,250,10,'white')



c1 = Circle(375,300,25,'white')
c2 = Circle(360,300,20,'white')
c3 = Circle(390,300,20,'white')
c4 = Circle(410,300,10,'white')

#太阳
sun = Circle(410,430,40,'yellow')


def draw1():
    
    #背景
    Rectangle(0, 0, 500, 500, "cyan").draw()
    
    #太阳
    sun.draw()
    
    #云朵
    a1.draw()
    a2.draw()
    a3.draw()
    a4.draw()


    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    window.show_axis()

