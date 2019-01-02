from pyleap import *
import random
import time
import math


#设置游戏区域大小
window.set_size(600, 600)

window.set_caption("雷霆战机")

enemy = Sprite('https://r.leaplearner.com/i/7686bf.png')
rock = Sprite('https://r.leaplearner.com/i/4a165e.png')

#保护罩
defend = Sprite('https://r.leaplearner.com/i/24dc6b.png')
speck = Sprite('https://r.leaplearner.com/ud/production/958096/5Mex.png',640,random.randint(0, 600))
defend.scale = 2

#设置背景图片、player图片和爆炸效果
background = Sprite("https://r.leaplearner.com/ud/production/958096/koZU.png",350,475)
background1 = Sprite("https://r.leaplearner.com/ud/production/958096/CTRe.png",350,1436)
background.h = 643
background.w = 501
background1.h = 642
background1.w = 501
player = Sprite("https://r.leaplearner.com/ud/production/958096/QKiT.png")
#改变敌人和战机大小
player.scale = 0.6
enemy.scale = 0.3
#闪屏
shan = Sprite('https://r.leaplearner.com/ud/production/958096/M44i.png')
shan.scale = 1

#保护罩大小
#defend.scale = 0.5

background.scale = 1.5
background1.scale = 1.5

boomscale = 0.3            
playerscale = 0.5          
boom = Sprite("https://llcs-1252287760.cossh.myqcloud.com/images/Boom2.png")
#改变爆炸大小
boom.scale = 0.5

boom_rock = Sprite('https://r.leaplearner.com/i/0c4952.png')
boom_rock.scale = 0.5

#设置敌人总部
player.bullets = []
enemys = []
temp_enemys = []
rock_rocks = []  #陨石


#设置得分
player.score = 0
score_txt = Text("得分：", 10, 540)


#游戏结束标语
retry_txt = Text("GAME OVER!!!", 200, 400, font_size=30)


#设置游戏时间
start_time = time.time()
time_txt = Text("剩余时间：" + str(math.floor(30 - (time.time() - start_time))), 10, 560)
global game_over
game_over = False

#子弹工厂
def emit_bullet(dt):
    bullet = Sprite('https://r.leaplearner.com/ud/production/958096/kUnZ.png', player.x, player.y)
    bullet.scale = 0.5
    player.bullets.append(bullet)


#敌机工厂
def new_enemy(dt):
    enemy1 = Sprite(enemy.src, random.randint(0, 600), 600)   #3\4   5\6
    enemy1.scale = enemy.scale
    enemy1.speed = random.randint(3,5)
    enemys.append(enemy1)

#陨石工厂
def emit_rock(dt):
    a = random.randint(1,4)
    rock1 = Sprite('https://r.leaplearner.com/ud/production/958096/8Upk.png',0, random.randint(400, 600))
    rock1_1 = Sprite('https://r.leaplearner.com/ud/production/958096/8Upk.png',random.randint(100, 400), 600)
    rock2 = Sprite('https://r.leaplearner.com/ud/production/958096/6zSV.png',0, random.randint(500, 600))
    rock2_2 = Sprite('https://r.leaplearner.com/ud/production/958096/6zSV.png',random.randint(100, 400), 600)
    rock1.scale = random.randint(2,3) / 10
    rock1_1.scale = random.randint(2,3) / 10
    rock2.scale = random.randint(2,3) / 10
    rock2_2.scale = random.randint(2,3) / 10
    rock1.xs = random.randint(2,2)
    rock1.ys = random.randint(-5,-3)
    rock1_1.xs = random.randint(2,2)
    rock1_1.ys = random.randint(-5,-3)
    rock2.xs = random.randint(2,2)
    rock2.ys = random.randint(-5,-3)
    rock2_2.xs = random.randint(2,2)
    rock2_2.ys = random.randint(-5,-3)
    if a == 1:
        rock_rocks.append(rock1)
    elif a == 2:
        rock_rocks.append(rock1_1)
    elif a == 3:
        rock_rocks.append(rock2)
    elif a == 4:
        rock_rocks.append(rock2_2)


#在窗口中绘制角色
def draw():
    #window.clear()
    #background.draw()
    #background1.draw()
    
    for enemy in enemys:
        enemy.draw()
        
    for bullet in player.bullets:
        bullet.draw()

    for rock in rock_rocks:
        rock.draw()

    player.draw()

    #开局5秒保护罩、之后消失、获取。
    if math.floor(time.time() - start_time) <= 5:
       defend.x = player.x
       defend.y = player.y
       defend.draw()
    elif math.floor(time.time() - start_time) > 5:
        if speck.collide(player):
            speck.y = 2500
        else:
            #speck.scale = 0.5
            speck.y -= 5
            speck.draw()
            if speck.y < -40:
                speck.y = 640
                speck.x = random.randint(0, 600)
                
        if speck.y > 1100:
            #defend.scale = player.scale * 0.85
            defend.x = player.x
            defend.y = player.y
            defend.draw()
        else:
            defend.y = -500
            defend.draw()

       
    score_txt.draw()
    time_txt.draw()


#让窗口中的角色运动
def update():
    global timer
    #控制player 跟随 mouse
    player.x =  mouse.x
    player.y =  mouse.y
    for enemy in enemys:
        enemy.y -= enemy.speed

    for bullet in player.bullets:
        bullet.y += 10

    for rock in rock_rocks:
        rock.y += rock.ys
        rock.x += rock.xs
            
    score_txt.src = "得分：" + str(player.score)
    time_txt.src = "剩余时间：" + str(math.floor(30 - (time.time() - start_time)))

#背景函数
def bg_run():
    window.clear()
    #防护罩实现，跟随飞机改变大小
    
    
    background.y -= 1
    background1.y -= 1
    if background.y < -475:
        background.y = 1436
    if background1.y < -475:
        background1.y = 1436
    background.draw()
    background1.draw()

    
#计算得分，删除敌机与子弹
def enemy_is_hit():
    try:
        #击中敌机
        for enemy in enemys:
            for bullet in player.bullets:
                p = bullet.collide(enemy) #子弹击中敌机
                p1 = defend.collide(enemy) #保护罩击中敌机
                if p1:
                    enemys.remove(enemy)
                    return True
                elif p:
                    enemys.remove(enemy)
                    player.bullets.remove(bullet)
                    return True
        #击中陨石
        for rock in rock_rocks:
            for bullet in player.bullets:
                p = bullet.collide(rock) #子弹击中敌机
                p1 = defend.collide(rock) #保护罩击中敌机
                if p1:
                    rock_rocks.remove(rock)
                    return True
                elif p:
                    rock_rocks.remove(rock)
                    player.bullets.remove(bullet)
                    return True
        
        return  False
    except:
        pass



#游戏引擎(发动机)1
def enemy_is_hit_a():
    try:
        #击中敌机特效
        for enemy in enemys:
            for bullet in player.bullets:
                p = bullet.collide(enemy) #子弹击中敌机
                p1 = defend.collide(enemy) #保护罩击中敌机
                if p1:
                    boom.x = p1.x
                    boom.y = p1.y
                    boom.draw()
                elif p:
                    boom.x = p.x
                    boom.y = p.y
                    boom.draw()
        #子弹优化
        for bullet in player.bullets:
            if bullet.y > window.h:
                player.bullets.remove(bullet)
        #敌机优化
        for enemy in enemys:
            if enemy.y < 0:
                enemys.remove(enemy)
        #击中陨石特效
        for rock in rock_rocks:
             for bullet in player.bullets:
                 p = bullet.collide(rock) #子弹击中敌机
                 p1 = defend.collide(rock) #保护罩击中敌机
                 p2 = player.collide(rock) #飞机撞击陨石
                 if p1:
                     boom_rock.x = p1.x
                     boom_rock.y = p1.y
                     boom_rock.draw()
                 elif p:
                     boom_rock.x = p.x
                     boom_rock.y = p.y
                     boom_rock.draw()
                 elif p2:
                     boom_rock.x = p2.x
                     boom_rock.y = p2.y
                     boom_rock.draw()
                     shan.draw()
        #陨石优化
        for rock in rock_rocks:
            if rock.y < 0:
                rock_rocks.remove(rock)
        for rock in rock_rocks:
            if rock.x > 600:
                rock_rocks.remove(rock)

    except:
        pass

def logic():
    global game_over
    
    #判断时间是否小于1，进行游戏结束,保护罩除外。
    for enemy in enemys:
        if defend.collide(enemy):
            pass
        elif player.collide(enemy):
            game_over = True
        if math.floor(30 - (time.time() - start_time)) < 0:
            game_over = True
    #判断是否碰到陨石，扣分
    for rock in rock_rocks:       
        if player.collide(rock):
            rock_rocks.remove(rock)
            player.score -= 2


#游戏引擎（发动机）2            
def game(dt):
    global game_over
    if(game_over):
        retry_txt.draw()
    else:
        bg_run()
        draw()
        enemy_is_hit_a()
        update()
        logic()
        if enemy_is_hit():    
            player.score += 2

#设置陨石出现频率
repeat(emit_rock,0.8)
#运行游戏
repeat(game,1/50)

#retry_txt.on_press(retry)
#run()
