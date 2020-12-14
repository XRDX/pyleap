from pyleap import *
import random
import time
import math

window.set_size(400, 600)  # 设置窗口大小
window.keep_on_top()

bg = Sprite("https://rss.leaplearner.com/Image/Bgs/bluebg.jpg")
player = Sprite("https://rss.leaplearner.com/Image/Role/Fighter13.png", 300, 300)
boom = Sprite("https://llcs-1252287760.cossh.myqcloud.com/images/Boom2.png", 0, 0, 150, 100)

bullet_src = "https://r.leaplearner.com/i/24dc6b.png"
enemy_src = "https://rss.leaplearner.com/Image/Role/Fighter12.png"
enemys_batch = Batch()
bullets_batch = Batch()

# 敌人列表
enemys = []
start_time = time.time()

# 我方子弹列表
player.bullets = []

player.score = 0
timer = 0

score_txt = Text("得分：", 10, 760)
retry_txt = Text("RETRY!", 200, 100, font_size=30)
time_txt = Text("剩余时间：" + str(60 - timer), 10, 720)

    
# 绘制函数
def draw():
    global enemys
    
    window.clear()
    bg.draw()
    player.draw()
    
    enemys_batch.draw()
    bullets_batch.draw()

    window.show_fps()


@window.event
def on_draw():
    global timer

    player.x = mouse.x
    player.y = mouse.y


    for enemy in enemys:
        enemy.y -= 2

    for bullet in player.bullets:
        bullet.y += 10
    
    draw()

    for enemy in enemys:
        if enemy.collide(player) or (60 - timer) < 0:
            retry_txt.draw()
            stop(game)

        for bullet in player.bullets:
            p = bullet.collide(enemy)
            if p:
                boom.x = p.x
                boom.y = p.y
                boom.draw()
                player.score += 1
                
                # to be removed
                enemy.y = -100
                bullet.y = 1000

    for enemy in [obj for obj in enemys if obj.y < -50]:
        enemy.delete()
        enemys.remove(enemy)

    for bullet in [obj for obj in player.bullets if obj.y > 800]:
        if bullet.y > 800:
            bullet.delete()
            player.bullets.remove(bullet)

    score_txt.src = "得分：" + str(player.score)

    
    if timer > 60:
        stop(game)
        
    time_txt.src = "剩余时间：" + str(60 - math.floor(timer))
    time_txt.draw()

    end_time = time.time()
    timer = end_time - start_time

def retry():
    global timer
    global enemys
    player.score = 0
    timer = 0
    enemys = []
    player.bullets = []
    player.x = mouse.x
    player.y = mouse.y
    repeat(game)


def emit_bullet(dt):
    bullet = Sprite(bullet_src, player.x-40, player.y, 20, 20, batch=bullets_batch)
    player.bullets.append(bullet)
    bullet = Sprite(bullet_src, player.x+40, player.y, 20, 20, batch=bullets_batch)
    player.bullets.append(bullet)

def new_enemy(dt):
    enemy = Sprite(enemy_src, random.randint(50, 350), 650, 100, 60, batch=enemys_batch)
    enemys.append(enemy)


retry_txt.on_press(retry)

repeat(emit_bullet, 0.05)
repeat(new_enemy, 0.2)

run()
