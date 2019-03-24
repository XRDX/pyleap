## pyleap简介

pyleap是由LeapLeaner开发的基于python的一个插件，有了pyleap，我们就可以在浏览器上使用简单的一些命令进行动画的创作，开发各种小游戏等。利用pyleap学习python，可以让你在学习python的过程中充满乐趣。

### 【推荐】使用立乐在线

下载地址： [windows](https://rss.leaplearner.com/assets/leaponline/win32/立乐在线 Setup 0.1.0.exe) [mac](https://rss.leaplearner.com/assets/leaponline/win32/立乐在线-0.1.0.dmg)

下载安装后，要尝试pyleap，只要打开软件，切换到python模式，点击运行，就可以看到效果了！在第一次打开这个页面时，我们已经为你创建了默认的代码，你可以尝试着去修改代码中的数字，来看看每个数字代表什么含义。

![weilcome](../images/introduction/weilcome.png)


### 独立的pyleap运行环境

#### 安装pyleap

首先，确保你已经安装了python3.x版本，然后使用命令行安装pyleap模块以及网页pyleap运行环境的，命令为

```shell
pip install pyleap
```

安装过程中会前置库pyglet、leapserver。

#### 使用pyleap

在代码中引入pyleap即可使用pyleap所带的功能

```python
from pyleap import *
```

