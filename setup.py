from setuptools import setup

setup(name='leap',
      version='0.1',
      description='A simple 2D game engine base on pyglet',
      url='http://github.com/XRDX/pyleap',
      author='Vic Wang',
      author_email='305880887@qq.com',
      license='BSD',
      packages=['leap'],
      install_requires=[
          'pyglet',
      ],
      zip_safe=False)
