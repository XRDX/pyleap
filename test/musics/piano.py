from pyleap import *


def press():
    print("a press")

def release():
    print("a release")

key.a.on_press(press)
key.A.on_release(release)

def a_value(dt):
    print(key.a.pressed)

repeat(a_value, 1)

run()