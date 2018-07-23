## 音乐与音效对象

好的项目离不开音效，合适的音效可以让一个项目发挥出200%的效果。

```javascript
var music = new Audio();
music.src = "ddd.mp3"
music.play();
```

属性和方法

src
获取或者设置音乐链接地址

oncanplaythrough
在音效加载结束后使用该方法

### 音乐

背景音乐一般是长度较长的音乐，且需要循环播放。我们可以将音效的`loop`属性设置为`true`，这样只要播放一次就可以了。

```javascript
var music = new Audio();
music.src = "ddd.mp3"
music.loop = true;
music.play();
```

### 音效

无论是音乐还是音效，浏览器在加载时都需要耗费一定的时间，因此一般都是通过异步加载的。因此只有在加载结束后才能进行播放。一般通过`oncanplaythrough`函数来调用播放音效。

如果是音效，我们可以在项目执行之前进行加载。本书不涉及到资源的管理和加载，如果有兴趣，可以去网上了解更多预加载的知识。

##### 实例：色阶钢琴

```javascript
var url = "http://llcs-1252287760.cossh.myqcloud.com/Piano/";

var urls = [ "40-C.mp3", "42-D.mp3", "44-E.mp3", "45-F.mp3", "47-G.mp3", "49-A.mp3", "51-B.mp3"];

var Key = Rectangle;
Key.prototype.click = function(){
    //this.audio.currentTime = 0;
    this.audio.play();
};

for(var i=0; i<urls.length; i++){
    var key = new Key(0, 550/7*i, 350, 550/7);
    key.fillStyle = RGB(0, 200-20*i, 200-20*i);
    key.audio = new Audio();
    key.audio.src = url + urls[i];
    key.fill();
}
```

