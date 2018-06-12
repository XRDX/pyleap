from pyleap import *

def draw(dt):
    Line(100, 100, 300, 200, 1, 'pink').draw()
    Line(100, 200, 300, 300, 2, 'red').draw()
    Line(100, 300, 300, 400, 4, 'green').draw()
    Line(100, 400, 300, 100, 10, 'white').draw()

schedule_interval(draw)
run()