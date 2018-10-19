import pyglet
from pyglet import gl

window = pyglet.window.Window(resizable=True)

@window.event
def on_draw():
    # x, y, z
    gl.glLoadIdentity()
    gl.glTranslatef(100, 100, 0)
    gl.glScalef(1.0, 1.0, 1.0)
    gl.glRotatef(30, 0.0, 0.0, 1.0)
    gl.glTranslatef(-100, -100, 0)

    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2f', (100, 100,
                 150, 100,
                 150, 150,
                 100, 150),
        (''))
    )


pyglet.app.run()
