# pyleap使用手册

### 安装 Install

```shell
pip install pyleap
```

如果要配合code.leaplearner使用，还需要安装leapserver模块。

```shell
pip install leapserver
```

### 使用 Usage

在项目中引入pyleap即可使用pyleap相关的功能

```python
from pyleap import *
```

在每次使用code环境钱，启动leapserver模块。

```shell
python -m leapserver
```



upload to pypi

```shell
$ python setup.py sdist bdist_wheel
$ twine upload dist/* -u VicWang -p PYPI******
```

pyinstaller

```shell
$ pyinstaller -F leap_server.py -i pyleap.ico
```



