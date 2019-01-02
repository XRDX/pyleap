from pyleap import *
window.set_size(500, 500)
def logo():
    #定义字体
    Text('School Bus',290,225,20,'white').draw()
    #定义车身上的线
    Line(295, 260, 425, 260, 3, 'black').draw()
    Line(295, 250, 425, 250, 3, 'black').draw()
    window.show_axis()
#背景
def bg():
    Rectangle(0, 0, 500, 500, 'cyan').draw()

