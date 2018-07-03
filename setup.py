import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyleap",
    version="0.0.9",
    author="Vic Wang",
    author_email="305880887@qq.com",
    description='A simple 2D game engine base on pyglet',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/XRDX/pyleap',
    packages=setuptools.find_packages(),
    install_requires=[
        'pyglet',
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)
