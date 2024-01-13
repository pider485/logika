#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, player_width, player_height,player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed
        
        self.width = player_width
        self.height = player_height
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - self.width-10: 
            self.rect.x += self.speed

    def fire(self):
        bullet=Bullet('bullet.png', self.rect.centerx-7,self.rect.top , 15, 20,15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>win_height:
            self.rect.y=0
            self.rect.x=randint(0,win_width-100)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y < -5:
            self.kill()

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_width, wall_height,collor):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(collor)
        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height= 500
bullets = sprite.Group()
monsters = sprite.Group()
commet = sprite.Group()
Ship = sprite.Group()

for i in range(5):
    en = Enemy('ufo.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
    monsters.add(en)

for i in range(2):
    en = Enemy('asteroid.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
    commet.add(en)


window = display.set_mode((win_width, win_height))
background = scale(load('galaxy.jpg'), (win_width, win_height))

ship = Player('rocket.png', 5, win_height-110, 80, 100, 9)
Ship.add(ship)
game= True
finish = False

clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.10)

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 80)
font3 = font.SysFont('Arial', 15)

txt_lose_game= font2.render('YOU LOSE!', True,(255,0,0))
txt_win_game= font2.render('YOU WIN!', True,(0,0,255))

txt_lose = font1.render(f'Пропущено: {lost}', True,(255,255,255))
txt_score =font1.render(f'Бали: {score}', True,(255,255,255))
max_ammo=5
ammo = 5
reload_ammo = 0

hp = 3

txt_ammo = font1.render(f'Патрони: {ammo}', True,(255,255,255))
txt_update = font3.render(f'збільшити кількість боєприпасів 5 б', True,(255,255,255))
txt_update1 = font3.render(f'Натисніть л для покупки', True,(255,255,255))
txt_update_hp = font3.render(f'Збільшити кількість життя 2 б', True,(255,255,255))
txt_hp = font3.render(f'Життя : {hp}', True,(255,255,255))
txt_hp_buy = font3.render(f'Натисніть О', True,(255,255,255))

noclip = False
nocllip_ind = Wall(5,5,10,10,(0,225,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_x:
                if ammo != 0:
                    ship.fire()
                    ammo-=1
            if e.key == K_r:
                ammo=0
            if e.key == K_k:
                if score >= 5:
                    max_ammo+=1
                    score -= 5
            if e.key == K_j:
                if score >=2:
                    hp+=1
                    score-=2
            if noclip == False:    
                if e.key == K_n:
                    noclip=True
                    nocllip_ind = Wall(5,5,10,10,(225,0,0))
            if noclip == True:    
                if e.key == K_m:
                    nocllip_ind = Wall(5,5,10,10,(0,225,0))
                    noclip=False
    if not finish:
        window.blit(background, (0, 0))
        txt_lose = font1.render(f'Пропущено: {lost}', True,(255,255,255))
        txt_score =font1.render(f'Бали: {score}', True,(255,255,255))
        txt_ammo = font1.render(f'Патрони: {ammo}', True,(255,255,255))
        txt_update = font3.render(f'збільшити кількість боєприпасів 5 б', True,(255,255,255))
        txt_update1 = font3.render(f'Натисніть л для покупки', True,(255,255,255))
        txt_hp = font3.render(f'Життя : {hp}', True,(255,255,255))
        txt_update_hp = font3.render(f'Збільшити кількість життя 2б', True,(255,255,255))
        txt_hp_buy = font3.render(f'Натисніть О', True,(255,255,255))
        window.blit(txt_lose, (10, 50))
        window.blit(txt_score, (10, 100))
        window.blit(txt_ammo,(500,50))
        window.blit(txt_update,(450,100))
        window.blit(txt_update1,(450,120))
        window.blit(txt_update_hp,(450,140))
        window.blit(txt_hp_buy,(450,160))
        window.blit(txt_hp,(450,180))
        ship.reset()
        ship.update()
        monsters.draw(window)
        monsters.update()

        commet.draw(window)
        commet.update()
        
        
        bullets.draw(window)
        bullets.update()
        
        nocllip_ind.reset()
        
        if noclip == False:
            if sprite.spritecollide(ship,commet,False):
                finish= True
                window.blit(txt_lose_game, (200,200))

            if hp == 0:
                finish= True
                window.blit(txt_lose_game, (200,200))

        collide = sprite.groupcollide(monsters,bullets,True,True)
        for c in collide:
            en = Enemy('ufo.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
            monsters.add(en)
            score+=1
        if noclip == False:
            collide = sprite.groupcollide(monsters,Ship,True,False)
            for c in collide:
                en = Enemy('ufo.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
                monsters.add(en)
                score+=1
                hp-=1
            collide = sprite.groupcollide(commet,Ship,True,False)
            for c in collide:
                en = Enemy('asteroid.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
                commet.add(en)
                score+=1
                hp -=1
        if ammo ==0:
            reload_ammo+=1
            print(reload_ammo)
            if reload_ammo == 80:
                ammo = max_ammo
                reload_ammo =0
            
        if score == 50:
            finish = True
            window.blit(txt_win_game, (200,200))
    else:
        score = 0
        lost = 0
        finish =False
        hp = 3
        
        for m in monsters:
            m.kill()
        
        for m in bullets:
            m.kill
        
        for m in commet:
            m.kill()
        
        time.delay(3000)

        for i in range(5):
            en = Enemy('ufo.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
            monsters.add(en)
        for i in range(2):
            en = Enemy('asteroid.png', randint(0,win_width-100), 0, 100, 80, randint(1,5))
            commet.add(en)
        
    display.update()
    clock.tick(FPS)