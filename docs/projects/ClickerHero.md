# 点击英雄

## 教学阶段

### 项目体验

打开网址：[http://ide.leaplearner.com/lmumov/1](http://ide.leaplearner.com/lmumov/1)，或者扫描一下二维码体验项目

![](../images/clicker.png)

### 开发环境

打开网址: [http://ide.leaplearner.com/jincai/1/edit](http://ide.leaplearner.com/jincai/1/edit?js,output)，点击`projects`->`clone`开始自己的项目。记录网址中间的这一串6个特殊字符，它是每个人项目的标示。

在IDE中我们添加了一些代码，是一些我们将要使用的资源地址，建议保留。

### IDE介绍

下面是立乐IDE的一个截图，如果和截图不一样没关系，点击上面的标签名称就可以打开或者关闭对应的页签。介绍几个主要区域：

- `JavaScript`区域，这里是代码区域，也是我们输入代码的地方，是最重要的地方
- `Output`区域，这里是展示区域，用于展示输出效果

![ide](../images/ide.png)

`Share`: 点击后生成链接和二维码，可以通过手机扫描获取到项目展示信息。

`Run`: 点击后执行JavaScript代码。每次点击`Run`都会重新开始执行。

`Auto-run`: 勾选后，只要修改代码便会自动执行代码。

`↗`：点击后在打开一个新页签，展示项目。

`html`：描述网页内容的的。

`console`：控制台，在激活状态下，会将日志信息和报错信息输出到这里。

`css`: 用于配置网页的样式，在本书中暂不涉及。

### 坐标介绍

为了定义空间的位置，数学家们发明了坐标的概念，在此至上发展出了庞大的几何学科。在计算机图形中，坐标系统更是不可或缺。

我们将左上角的坐标定义为`(0,0)`，把水平轴为`x轴`，把垂直坐标定义为`y轴`。平面上的任意一个点，在`x轴`上的投影称之为该点的`x坐标`，同样，在`y轴`上的投影即`y坐标`。因此，整个坐标系看起来像是这个样子的。

![pos_xy](../images/axis.png)

只要确定了坐标点的值，我们就能很容易的确定坐标的位置了。

> 小知识：笛卡尔坐标系和网页坐标系
>
> 和数学上常见的笛卡尔坐标系不同的是，网页坐标系的y轴正方向朝下。这是因为人类阅读习惯于从左到右，从上到下，在浏览器的定位系统中，根据这个习惯来定义坐标的位置，使得在网页设计时更为合理。

### 插入图片

用到了Sprite这个类，它的定义是这样的。

```javascript
Sprite(url, x, y, width, height)
```

* `url`，是图片的地址，一般以`jpg`或者`png`结尾
* `x`、`y`，图片左上角的横坐标和纵坐标
* `width`、`height`，图片在画布上显示的宽度和高度

最后，使用图片对象的`draw`方法将图片绘制在画布上。

```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 150, 100, 50, 50);
bg.draw();
item.draw();
```

点击执行，就可以将这两张图片绘制在画布上了。

### 行动起来

接下来，就是让物体开始运动起来了。画布上，我们每隔一段时间`(16.7ms)`将图形重新绘制一次，因为频率非常块，看起来就像是动起来一样。

这里我们需要先定义一个`GameLoop`函数，它的作用是在每一帧里绘制图形，同时在下一帧中调用自己。

```javascript
function GameLoop(){
    item.y += 1;
  
    bg.draw();
    item.draw();
    nextFrame(GameLoop);
}

loadRssAndRun(GameLoop);
```

在`GameLoop`中，我们让物体的y值每次都增加一，以达到每次往下移动的效果。最后，我们用一个函数`loadRssAndRun(GameLoop);`来加载图片并且开始执行这个循环。

完整代码如下：

```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 150, 100, 50, 50);

function GameLoop(){
    item.y += 1;
  
    bg.draw();
    item.draw();
    nextFrame(GameLoop);
}

loadRssAndRun(GameLoop);
```

### 点击事件

在点中物体时，我们需要让物体消失，然后刷新出一个新的物体。事实上，我们不用这么麻烦，把物体的坐标修改为0就可以了。

```javascript
item.click = function(){
    item.y = 0;
};
```

### 随机位置

每次都是固定的位置显然不好玩，让我们同时修改下物体的水平位置，使用一个随机的概念。`Math.random()`会产生一个0到1的随机数，乘以300，即随机生成一个0到300的随机数。

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
};
```

### 显示分数

接下来就是记录游戏的分数了。让我们新增一个变量`score`，初始值为0。

```javascript
var score = 0;
```

数字是没法直接显示出来的，我们需要将数字转为字符串，利用JavaScript中字符串＋数字，自动将数字转为字符串的特性，我们可以实现数字的转换。

```javascript
var scoreMsg;

function GameLoop(){
    item.y += 1;
    scoreMsg = "score:" + score;
  
    bg.draw();
    item.draw();
    scoreMsg.draw();
    nextFrame(GameLoop);
}
```

当然，别忘了在成功点击物体时增加分数，否则分数就不会增加啦。

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
    score++;
};
```

完整代码如下

```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 150, 100, 50, 50);

var score = 0;
var scoreMsg;

function GameLoop(){
    item.y += 1;
    scoreMsg = "score:" + score;
  
    bg.draw();
    item.draw();
    scoreMsg.draw();
    nextFrame(GameLoop);
}

loadRssAndRun(GameLoop);

item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
};
```

### 播放声音

没有声音，再好的戏也出不来。让我们来增加两个声音，背景音乐和点击音效，这里增加了两个新的声音对象

```javascript
var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";

var clickSound = new Audio();
clickSound.src = "http://llcs-1252287760.cossh.myqcloud.com/audio/gold.mp3";
```

背景音乐我们需要让它循环播放，因此设置`loop`属性为`true`

```javascript
var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";
bgm.loop = true;
bgm.play();
```

而物体点击音效则是在点击的时候播放，因此我们把它加在点击时

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
    clickSound.play();
};
```

最终代码

 ```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 150, 100, 50, 50);

var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";
bgm.loop = true;
bgm.play();

var clickSound = new Audio();
clickSound.src = "http://llcs-1252287760.cossh.myqcloud.com/audio/gold.mp3";

var score = 0;
var scoreMsg;

function GameLoop(){
    item.y += 1;
    scoreMsg = "score:" + score;
  
    bg.draw();
    item.draw();
    scoreMsg.draw();
    nextFrame(GameLoop);
}

loadRssAndRun(GameLoop);

item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
    clickSound.play();
};
 ```

### 代码重构

在进入下一章节前，我们先对我们的程序进行一个小小的重构。在改变速度这里，我们使用了这么一行代码

 ```javascript
item.y += 1;
 ```

 这里1代表的是速度，但是并不直观。所以我们定义一个变量`speed`来表达它。

```javascript
var scoreMsg;
var speed = 1;
...
    item.y += speed;
```

### 难度提升

接下来，就是我们对游戏的难度进行修改。我们在每一次分数增加的时候去提高物体掉落的速度，这样就能提高游戏难度了！

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
    speed += 1;
    clickSound.play();
};
```

如果你觉得难度变化太大，你可以降低这个数值，让速度的增长变的慢一点。

### 游戏结束

游戏结束时，我们在屏幕上写上Game Over。

```javascript
function GameOver(){
    'Game Over'.draw(120, 300, "white");
}
```

怎么判断游戏结束呢，先用一段伪代码来表示

```javascript
如果物体超出了画布:
    游戏结束
其他情况下：
	继续游戏循环
```

在JavaScript中，就可以写成

```javascript
function GameLoop(){
    ...
    if(item.y > canvas.height)
    	GameOver();
	else
    	nextFrame(GameLoop);
}
```

### 重新开始

重新开始游戏循环前，我们要做这几件事情

* 把分数清零
* 把物体放回到最上方
* 把速度变为最初的速度

最后执行游戏循环。

```javascript
function GameStart(){
    score = 0;
    item.y = 0;
    speed = 1;
    GameLoop();
}
```

那什么时候触发游戏重新开始呢，当然是游戏结束的时候了。我们需要在游戏结束时添加一个按钮来激活它。

```javascript
var retry = new Sprite( "http://osykyzwcn.bkt.clouddn.com/SHAYUx0001.png", 120, 300, 100, 50);
retry.click = GameStart;

function GameOver(){
    "Game Over".draw(120, 160, "white");
	retry.draw();    
}
```

当游戏结束的时候，这个按钮就会被绘制到画布上，点击就可以重新开始游戏啦。

最终代码

```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 100, 0, 60, 60);

var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";
bgm.loop = true;
bgm.play();

var sound = new Audio();
sound.src = "http://llcs-1252287760.cossh.myqcloud.com/audio/gold.mp3";

var speed = 1;
var score = 0;
var hiscore = 0;

item.click = function(){
    score += 1;
    speed += 1;

    sound.currentTime = 0;
    sound.play();

    item.y = 0;
    item.x = Math.random() * 300;
};

function GameStart(){
	item.y = 0;
    score = 0;
    speed = 1;
    GameLoop();
}

function GameLoop(){
    item.y += speed;
    
	bg.draw();
    item.draw();
    
    var scoreMsg = "Score: " + score;
    scoreMsg.draw();

  	if(item.y > canvas.height)
      GameOver();
  	else
      nextFrame(GameLoop);
}

var retry = new Sprite( "http://osykyzwcn.bkt.clouddn.com/SHAYUx0001.png", 120, 300, 100, 50);
retry.click = GameStart;

function GameOver(){
    "Game Over".draw(120, 160, "white");
	retry.draw();    
}

loadRssAndRun(GameStart);
```



## 挑战阶段

初级：

* 替换图片、音乐素材资源
* 修改游戏参数，调整游戏难度

中级：

* 让道具从其他方向出现
* 在界面上添加更多丰富的元素

高阶：

* 同时掉落更多道具
* 运动方向多样化