import pyglet

window = pyglet.window.Window()


@window.event
def on_draw():
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2i', (100, 100, 105, 100, 105, 300, 100, 300))
    )


pyglet.app.run()