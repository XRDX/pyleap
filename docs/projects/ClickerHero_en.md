# Clicker Hero

## Teaching Stage

### View the Project!

Open this URL：[http://ide.leaplearner.com/lmumov/1](http://ide.leaplearner.com/lmumov/1), Or scan the QR code to preview the project.

![](../images/clicker.png)

### Development environment

Open this URL: [http://ide.leaplearner.com/jincai/1/edit](http://ide.leaplearner.com/jincai/1/edit?js,output), Click `projects`->`clone`to start the project.
Record the string of 6 special characters in the middle of the URL, which is an
identification of everyone's project.

### IDE Introduction

The following is a screenshot of the IDE of LeapLearner, you can see three parts, from left to right are：

- `JavaScript`area: the code area. It is the most important part, where we enter the code.
- `Output`area: the display area. It is to demonstrate the output.

![ide](../images/ide.png)

`Share`: Click to generate link and QR code, you can share the project with others. Through the link or QR code, your friends can view your project.

`Run`: run the code. 

`Auto-run`: After checking this button, as long as the code is modified, the code will be automatically executed.

`↗`: Click to open a new tab page to present the project. 

`html`: it describes the content of the page.

`console`: In the activated state, the log information and error messages will be showed in console.

`css`: Used to configure the style of the page, not involved in this book.

### Introduction of Coordinates

In order to define the position of space, mathematicians invented coordinates, Based on coordinates, geometry was developed. In computer graphics, the coordinate system is indispensable.

We will define the coordinates of the upper left corner as `(0,0)`, The horizontal axis is  defined as the `x-axis`The vertical coordinate is defined as the `y-axis `. Any point in the plane, the projection on the `x-axis`is called the `x coordinate`, Similarly, the projection on the `y-axis` is the `y-coordinate`.Therefore, the coordinate system looks like this.

![pos_xy](../images/axis.axis

As long as we have the value of the coordinate point, we can easily determine its position. 

> Tips: Cartesian coordinate system and web coordinate system
>
> Unlike the mathematically common Cartesian coordinatesystem, the y-axis of the web page coordinate system is downward. This isbecause human reading habits is from left to right and from top to bottom, Define the location of coordinates according to this habit can make webpage design more reasonable.

### Insert a picture

The defination of Sprite is as follows:

```javascript
Sprite(url, x, y, width, height)
```

* url: the address of the picture.
* x ,y: The horizontal and vertical coordinates of the upper left corner of the picture .
* width, height: the width and height of the picture showed on canvas.

```javascript
var bg = new Sprite("http://orjajlo36.bkt.clouddn.com/backgroundimage2.jpg", 0, 0, 350, 550);
var item = new Sprite("http://ou1htxdl4.bkt.clouddn.com/coin.png", 150, 100, 50, 50);
bg.draw();
item.draw();
```

Finally, use `draw` to insert a picture on canvas. Click on `Run` , you can draw these two pictures on the
canvas.

### Move it!

Let’s make the object move!.In canvas, every 16ms we draw the graph again. Because of the fast frequency switching, it looks like it is moving.

We need to define a function `GameLoop`. Its purpose is to draw the graph in each frame and call itself in the next frame.

```javascript
function GameLoop(){
    item.y += 1;
  
    bg.draw();
    item.draw();
    nextFrame(GameLoop);
}

loadRssAndRun(GameLoop);
```

In `GameLoop`We increase the y value of the object by one each time to achieve the effect of moving

 down. Finally, we use the function  `loadRssAndRun(GameLoop); ` to load the picture.

The complete code is as follows:

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

### Click event

When clicking the item, we need to make the object disappear, and then refresh a new object. In fact, we can make it easier by changing the coordinates of the object to zero.

```javascript
item.click = function(){
    item.y = 0;
};
```

### Random position

Obviously it is not fun with the fixed position. Let's modify the horizontal position of the object at the same time, using Random.`Math.random() `will produce a random number from 0 to 1. Multiply by 300, it will produce a random number from 0 to 300.

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
};
```

### Score

Thenext step is to record the game's score Add a variable `score`. The initial value is 0.

```javascript
var score = 0;
```

The numbers can not be displayed directly. We need to convert the numbers to strings. Using the string + numbers in JavaScript, the numbers can be automatically converted to strings. 

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

Hey, remember to increase the score when you successfully click on an object, or the score will not increase.

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
    score++;
};
```

The complete code is as follows:

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

### Sound

Adding sound to our program is to make the game more interesting. Let's add two sounds: the background music and the click sound effect

```javascript
var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";

var clickSound = new Audio();
clickSound.src = "http://llcs-1252287760.cossh.myqcloud.com/audio/gold.mp3";
```

We need the background music play in a continuous loop.

```javascript
var bgm = new Audio();
bgm.src = "http://oq2qlcey8.bkt.clouddn.com/bgm.mp3";
bgm.loop = true;
bgm.play();
```

The sound effect of clicking item is played when clicked, so we add it to the click.

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
    clickSound.play();
};
```

Final Code

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

### Reconstruct

Before moving on to the next chapter, let's make a slight adjustment to our program. Here's a line of codethat changes speed.

 ```javascript
item.y += 1;
 ```

Here `1` represents the speed, but it is not clear enough. So we define a variable `speed` to express it more intuitively.

```javascript
var scoreMsg;
var speed = 1;
...
    item.y += speed;
```

### Challenge

Next, let’s modify the difficulty of the game. We
increase the speed every time we score, which will increase the difficulty of the game!

```javascript
item.click = function(){
    item.y = 0;
    item.x = Math.random() * 300;
	score++;
    speed += 1;
    clickSound.play();
};
```

If you feel that the game becomes too difficult, you can lower this value and let thespeed increase slowly.

### Game over

At the end of the game, we wrote Game Over on the screen.

```javascript
function GameOver(){
    'Game Over'.draw(120, 300, "white");
}
```

 How to judge the game is over or not? We need a pseudocode to determine it.

```javascript
If the object is beyond the canvas: 
	The game is over.
In other cases:
	Continue the game loop.
```

You can write it in JavaScript as follows:

```javascript
function GameLoop(){
    ...
    if(item.y > canvas.height)
    	GameOver();
	else
    	nextFrame(GameLoop);
}
```

Restart

Before restart the game loops,we need to:

* Clear the score
* Put the object back to the top 
* Change the speed to the original speed

Finally, run loops.

```javascript
function GameStart(){
    score = 0;
    item.y = 0;
    speed = 1;
    GameLoop();
}
```

When shall we restart the game? We need a button to make the game restart at the end of the game.

```javascript
var retry = new Sprite( "http://osykyzwcn.bkt.clouddn.com/SHAYUx0001.png", 120, 300, 100, 50);
retry.click = GameStart;

function GameOver(){
    "Game Over".draw(120, 160, "white");
	retry.draw();    
}
```

The button will be on the canvas when the game ends. You can click the button and restart the game then.

Final Code Line

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

## Free play

Primary level 

* Replace pictures, music assets
* Modify the game parameters, adjust the game difficulty

Advanced level:

* Let props appear from other directions.
* Add more elements to the interface. 

Senior level:

* Drop more props at the same time
* Diversify the direction of movement