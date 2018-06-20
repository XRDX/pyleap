from pyleap.window import window
from pyglet.window import key as default_key


keys = default_key.KeyStateHandler()
window.push_handlers(keys)

class Key():

    def __init__(self, keys):
        self.keys = keys

    def __getattr__(self, key_name):
        return keys[default_key.__dict__[key_name]]

key = Key(keys)