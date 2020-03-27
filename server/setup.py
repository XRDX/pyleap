import setuptools

# python setup.py sdist bdist_wheel
# twine upload dist/* -u VicWang -p PYPI******

setuptools.setup(
    name="leapserver",
    version="2020.3.27",
    author="Vic Wang",
    author_email="305880887@qq.com",
    description='a server for run python on web',
    long_description="a server for run python on web",
    long_description_content_type="text/markdown",
    url='http://github.com/XRDX/pyleap',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)
