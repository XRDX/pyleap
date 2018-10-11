import setuptools

# -$ python setup.py sdist bdist_wheel
# -$ twine upload dist/* -u VicWang -p PYPI******

setuptools.setup(
    name="pyleap",
    version="0.1.7",
    author="Vic Wang",
    author_email="305880887@qq.com",
    description='A simple 2D game engine base on pyglet',
    long_description='A simple 2D game engine base on pyglet',
    long_description_content_type="text/markdown",
    url='http://github.com/XRDX/pyleap',
    packages=setuptools.find_packages(),
    install_requires=[
        'pyglet',
        'leapserver',
        'leaptask'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)
