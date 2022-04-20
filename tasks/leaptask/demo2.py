from pyleap import *
import time 
import random
window.set_size(600, 600)#Set the windows size
#מגדירים דברים

player = Sprite("https://rss.leaplearner.com/Image/Role/Fighter13.png", 300, 300)  
bg = Sprite("https://r.leaplearner.com/i/83b8b6.jpg",300,300,600,600)
enemy  = Sprite('https://r.leaplearner.com/i/bfc571.png', 400, 700)
boss = Sprite('https://r.leaplearner.com/i/91b9d1.png',-1000,-1000)
pic1 = "https://r.leaplearner.com/i/bfc571.png"
pic2 = "https://r.leaplearner.com/i/06de0f.png"
pic3 = "https://r.leaplearner.com/i/6399c3.png"
pic4  = "https://r.leaplearner.com/i/d54440.png"
picb1 = "https://r.leaplearner.com/i/6be3c0.png"
picb2 = "https://r.leaplearner.com/i/20e9bb.png"
picb3 = "https://r.leaplearner.com/i/9ce8d8.png"
picb4 = "https://r.leaplearner.com/i/e96b44.png"
enemy_bullet  = Sprite('https://r.leaplearner.com/i/6be3c0.png',   enemy.x,enemy.y)
enemy_bullet2  = Sprite('https://r.leaplearner.com/i/6be3c0.png',   enemy.x,enemy.y)
player_bullet = Sprite('https://r.leaplearner.com/i/a6d418.png', player.x,player.y)
boss_bullet = Sprite("https://r.leaplearner.com/i/8895b1.png",boss.x,boss.y)
heart1 = Sprite('https://r.leaplearner.com/i/93196d.png',500,570)
heart2 = Sprite('https://r.leaplearner.com/i/93196d.png',520,570)
heart3 = Sprite('https://r.leaplearner.com/i/93196d.png',540,570)
heart4 = Sprite('https://r.leaplearner.com/i/93196d.png',500,570)
heart = Sprite('https://r.leaplearner.com/i/93196d.png',-1000,570)
boom = Sprite('https://r.leaplearner.com/i/5b7d5b.png',-1000,-1000)
meteor = Sprite('https://r.leaplearner.com/i/a88ff8.png',-1000,200)
res_b = Circle(310,210,60,"white")
#Audio("https://r.leaplearner.com/a/16/gameBG.mp3",True).play()

laser = Rectangle(boss.x,boss.y, 15, 0, 'red')
laser.state = -1
laser.speedy = 15

health_bar = Rectangle(-1000, 100, 15, 400, 'yellow')
health_bar.health = 5 


# מגדירים  מהירות ועושים פגיעות
enemy_bullet.speedx = random.randint(-2,3)
enemy_bullet.speedy = 7
enemy.speedy = 4
boss.speedx = 4
enemy.hit = 0

#מרזים את כל הדברים
meteor.scale = 1.5
boom.scale = 0.5
enemy.scale = 0.7
enemy_bullet.scale = 0.6
player_bullet.scale = 0.5
heart1.scale = 0.3
heart2.scale = 0.3
heart3.scale = 0.3
heart.scale = 0.2
boss.scale = 2

#מגדירים לשחקן את הרזות ומגדירים נקודות ולבבות
player.scale = 1  
player.lives = 3
player.score = 0
player.boss_comes = 5 # מתי שהבוס מגיע 
txt_score = Text("Score: 0",20,580)
txt_live = Text("Lives: 0",130,580)


txt_victory = Text("VICTORY", 140, 800, 60,'yellow')
# Is it possible to make it that the kids can write from here without seeing the rest of the code, to not intimidate them?

def game(dt):
    pass

@window.event
def on_draw():  
    #עושים ציור לדברים
    bg.draw()
    player_bullet.draw()
    enemy_bullet.draw()
    heart1.draw()
    heart2.draw()
    heart3.draw()
    heart.draw()
    txt_victory.draw()
    player.draw()
    enemy.draw()
    boom.draw()
    meteor.draw()
    boss_bullet.draw()
    laser.draw()
    boss.draw()
    health_bar.draw()

    if player.lives <= 0:
        Text("GAME OVER",110,300,50).draw()
    
    #עושים ציור לדברים וכותבים את הטקסט
#    txt_live.draw()
    txt_score.draw()

def update(dt):
#    txt_live.src = "Lives: " + str(player.lives)
    txt_score.src = "Score: " + str(player.score)
    
    #עושים שהעכבר ישלוט על שחקן 
    player.x = mouse.x
    player.y = mouse.y
    #עושים שהמטאור יזוז ושהלב יפול
    heart.y -= 8
    meteor.y -= 12
    
    #שהכדור של השחקן זז למעלה ואם הכדור של השחקן הגובה גדול מ600 אז הוא חוזר לשחקן 
    player_bullet.y += 5
    #if player_bullet.y > 600:
    #    player_bullet.x = player.x
    #    player_bullet.y = player.y
    
    # קובע מהירות נפילה לאויב וגם בודק אם הוא היגע למטה
    enemy.y -= enemy.speedy
    if enemy.y < 0:
        enemy.y = random.randint(650,800)
        enemy.x = random.randint(50,550)
    
    # שהכדור של האויב יורד למטה והכדור של האויב הוא מוגדר להיות עם מהירות ואם הכדור של האויב בגובה מתחת ל0 אז הוא חוזר לאויב 
    enemy_bullet.y -= enemy_bullet.speedy
    enemy_bullet.x += enemy_bullet.speedx
    if enemy_bullet.y < 0:
        enemy_bullet.y = enemy.y
        enemy_bullet.x = enemy.x
        enemy_bullet.speedx = random.randint(-2,3)
   
    #אם בדור של השחקן פוגע באויב אז יש בום והאויב חוזר למעלה ואיקס אקראי והכדור שלו חוזר עליו
    if enemy.collide(player_bullet):
        boom.x = enemy.x
        boom.y = enemy.y
        enemy.y = random.randint(650,800)
        enemy.x = random.randint(50,550)
        player_bullet.y = 1000
        player.score +=1
        enemy_bullet.x = enemy.x
        enemy_bullet.y = enemy.y
        enemy_bullet.speedx = random.randint(-2,3)
        enemy.hit += 1
        #Audio("https://r.leaplearner.com/a/5run/boom.mp3").play()
        if player.score % 5 == 0 and player.score >0:
            enemy_bullet.speedy += 0.5
            enemy.speedy += 0.5
    
        #בוחרים מספר אקראי שקובע איזה תמונה יש לאויב
        i = random.randint(1,5)
        if i == 1:
            enemy.src = pic1
        if i == 2:
            enemy.src = pic2
        if i == 3:
            enemy.src = pic3
        if i == 4:
            enemy.src = pic4
        if enemy.src == pic1:
            enemy_bullet.src = picb1
        if enemy.src == pic2:
            enemy_bullet.src = picb2
        if enemy.src == pic3:
            enemy_bullet.src = picb3
        if enemy.src == pic4:
            enemy_bullet.src = picb4
    
    
    # מתי שהכדור של האויב מתנגש בשחקן א6ז האויב חוזר למעלה ויורד
    if enemy_bullet.collide(player):
        enemy.y = 600
        if player.lives > 0:
            player.lives -= 1
        
        enemy_bullet.x = enemy.x
        enemy_bullet.y = enemy.y + 25
        enemy_bullet.speedx = random.randint(-2,3)
    
    #עושה שכל פעם שיורד לב אחד הלבבות נעלם
    if player.lives == 3:
        heart1.opacity = 1
        heart2.opacity = 1
        heart3.opacity = 1
    if player.lives == 2:
        heart1.opacity = 0.3
        heart2.opacity = 1
        heart3.opacity = 1
    if player.lives == 1:
        heart1.opacity = 0.3
        heart2.opacity = 0.3
        heart3.opacity = 1
    if player.lives == 0:
        heart1.opacity = 0.3
        heart2.opacity = 0.3
        heart3.opacity = 0.3


    #יש סיכוי של 2 ל1000 שיפול הלב וזה רק אם החיים שלו הם מתחת לשלוש
    if random.randint(0,1000) < 2 and player.lives < 3 and heart.x == -1000:
        heart.y = 700
        heart.x = random.randint(30, 540)
    if heart.y < -50:
        heart.x = -1000
    
    #אם הלב מתנגש בשחקן אז יש לו עוד לב
    if heart.collide(player) and player.lives < 3:
        heart.x = -1000
        player.lives +=1
        heart4.draw()
        #Audio("https://r.leaplearner.com/a/5/Btn_return.mp3").play()
    
    #אם הלבבות של השחקן הם 0 אז נגמר המשחק
    if player.lives <= 0:
        
        stop(update)
        # Text("GAME OVER",110,300,50).draw()
        #Rectangle(0,0,600,600,"green").draw()
        #Text("GAME OVER",110,300,50).draw()
        #res_b.draw()
        #Text("restart",250,200,30).draw()
        #time.sleep(5)
        
    
    # שמטאור משתגר רק אם האיקס שלו הוא  מינוס 1000 בגובה ואם יש 10 פגיעות ושהוא משתגר הוא בגובה 700 ובאיקס בין 50 ל550 
    if meteor.x == -1000 and enemy.hit % 4 == 0 and enemy.hit > 0:
        meteor.x = random.randint(50,550)
        meteor.y = 700
         
    
    #אם הגובה של המטאור הוא פחות ממינוס 100 אז האיקס שלו חוזר למינוס1000
    if meteor.y < -2000:
        meteor.x = -1000
    
    # המטאור פוגע בשחקן אז הוא הלבבות שלו חוזרות ל0
    if meteor.collide(player):
        player.lives = 0
    
    # בודק אם הגענו לניקוד הנכון ומשגר את הבוס אם הוא מוכן
    if player.score == player.boss_comes and boss.y == -1000:
        boss.x = 200
        boss.y = 550
        enemy.x = -1000
        enemy.speedy = 0
        enemy_bullet.x = enemy.x 
        boom.x = enemy.x 
        laser.state = 0 # מצב התחלה
        health_bar.x = 10
        
        
    if laser.state == 0:
        laser.x = boss.x
        laser.y = boss.y
        laser.h = 0 
        laser.state = 1
        
    boss.x += boss.speedx
    boss_bullet.y -= 7
    
    if boss.x > 570:
        boss.speedx = -4
    
    if boss.x < 30:
        boss.speedx = 4
        
    
    if laser.state == 1:
        laser.h -= laser.speedy
        if laser.h < -500: 
            laser.state = 2
    
    if laser.state == 2:
        laser.y -= laser.speedy
        if laser.y < 0:
            laser.state = 0
            
    
    if laser.collide(player):
        laser.state = 0
        player.lives -= 1
        
    
    if player_bullet.collide(boss):
        player_bullet.y = 1000
        
        health_bar.health -= 1
        health_bar.h = health_bar.health * 80
    
    
    if health_bar.health <= 0:
        boss.y = -2000
        txt_victory.y -= 5
    
    if txt_victory.y < -100: 
        stop(update)
        #Rectangle(0,0,600,600,"cyan").draw()
        #Text("YOU WIN",160,300,50).draw()
        #res_b.draw()
        #Text("PLAY AGAIN",252,200,14).draw()
        #Text("Made by Itay&Omer",250,59,10).draw()
        
    
    
    
#מגדירים פונקציה חדשה שפועלת רק כאשר לוחצים על העכבר    
def shoot():
    player_bullet.x = player.x
    player_bullet.y = player.y
    
def reset():
    enemy.hit = 0
    player.lives = 3
    player.score = 0
    enemy.speedy = 4
    enemy.y = 700
    enemy.x = 400
    enemy_bullet.speedy = 7
    enemy_bullet.x = enemy.x
    enemy_bullet.y = enemy.y
    boss.y = -1000
    laser.state = -1
    health_bar.health = 5
    health_bar.x = -1000
    laser.y = boss.y
    txt_victory.y = 800
    health_bar.h = 400
    boom.x = -1000
    
    
    
repeat(update)

#בלחיצת עכבר תפעיל פוקנציה שבסוגריים
mouse.on_press(shoot)
res_b.on_press(reset)    

if __name__ == "__main__":
    # repeat(game)   

    run()