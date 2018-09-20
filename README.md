# pyleap使用手册

### 安装 Install

```shell
pip install pyleap
```

### 使用 Usage

在项目中引入pyleap即可使用pyleap相关的功能

```python
from pyleap import *
```

在每次使用code环境前，启动leapserver模块。

```shell
python -m leapserver
```



### 更新

```shell
pip install pyleap --upgrade
```



### 打包

如果要将程序打包，可以安装pyinstaller

```shell
pip install pyinstaller
```

打包命令可以参照pyinstaller文档，如果要打成一个文件，按照以下指令，将my_file替换为自己的文件名。

```shell
$ pyinstaller -F my_file.py --windowed
```