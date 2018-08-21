# pyleap: A simple 2D game engine base on pyglet

install

```shell
pip install pyleap
pip install leap-server
```

usage

```shell
python -m leap_server
```

注意，安装包使用的是`-`，运行本地服务器使用的是下划线`_`。





upload to pypi

```shell
$ python setup.py sdist bdist_wheel
$ twine upload dist/* -u VicWang -p PYPI******
```

pyinstaller

```shell
$ pyinstaller -F leap_server.py -i pyleap.ico
```



