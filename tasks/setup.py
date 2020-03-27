import setuptools

# -$ python setup.py sdist bdist_wheel
# -$ twine upload dist/* -u VicWang -p PYPI******

setuptools.setup(
    name="leaptask",
    version="2020.3.27",
    author="Vic Wang",
    author_email="305880887@qq.com",
    description='leap task',
    long_description="leap tasks",
    long_description_content_type="text/markdown",
    url='http://github.com/XRDX/pyleap',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)
