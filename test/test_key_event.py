from pyleap import *


def press():
    print("a press")

def release():
    print("a release")

key_event.a.on_press = press
key_event.a.on_release = release

run();