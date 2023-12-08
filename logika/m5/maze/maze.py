#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint
from time import sleep


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = scale(load(player_image), (65, 65))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-70:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70: 
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
    
    direction_x = 'left'
    direction_y = 'up'
    def update_x(self):
        if self.direction_x == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed    
            
        if self.rect.x <= 450:
            self.direction_x = 'right'
        if self.rect.x >= win_width - 80:
            self.direction_x = 'left'
    def update_y(self):
        if self.direction_y == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed    
            
        if self.rect.y <= 1:
            self.direction_y = 'up'
        if self.rect.y >= win_width - 80:
            self.direction_y = 'down'
                
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
win_height = 500

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = Player('hero.png', 5, win_height - 80, 4)
cyborg = Enemy('cyborg.png', win_width - 150, win_height - 250, 4)
final = GameSprite('treasure.png', win_width - 80, win_height-80, 0)

Wall1 = Wall(20,20,670,40,(0,225,0))
Wall2 = Wall(210, 20, 40 ,250,(0,225,0))
Wall3 = Wall(90,300,40,200,(0,225,0))
Wall4 = Wall(340,300,90,200,(0,225,0))

game = True
finish = 1
clock = time.Clock()
FPS = 60



font.init()

f = font.Font(None, 70)
win = f.render('YOU WIN!', True,(255,215,0))
lose = f.render('YOU LOSE!', True,(255,1,1))




mixer.init()
mixer_music.load("jungles.ogg")
mixer.music.play(-1)

money_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

nocllip= 0
nocllip_ind = Wall(5,5,10,10,(0,225,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == 1:        
        window.blit(background,(0,0))
        player.reset()
        cyborg.reset()
        final.reset()
        Wall1.reset()
        Wall2.reset()
        Wall3.reset()
        Wall4.reset()
        nocllip_ind.reset()
        player.update()        
        cyborg.update()        
        
        if sprite.collide_rect(player, final):
            finish += 1
            window.blit(win, (200,200))
            money_sound.play()
            display.update()
            #sleep(2.5)
            player.rect.x = 19
            player.rect.y = 13       
            Wall1 = Wall(118,1,87,415,(0,225,0))
            Wall2 = Wall(270,1,87,415,(0,225,0))
            Wall3 = Wall(422,1,87,415,(0,225,0))
            Wall4 = Wall(574,1,87,415,(0,225,0))
            display.update()
            
        if key.get_pressed()[K_n] and nocllip == 0:
            nocllip = 1
            nocllip_ind = Wall(5,5,10,10,(225,0,0))
        if key.get_pressed()[K_m] and nocllip == 1 :
            nocllip = 0
            nocllip_ind = Wall(5,5,10,10,(0,225,0))
        if nocllip == 0 :    
            if sprite.collide_rect(player, cyborg):
                finish = 0
                window.blit(lose, (200,200))
                kick_sound.play()

            if sprite.collide_rect(player, Wall1) or sprite.collide_rect(player, Wall2) or sprite.collide_rect(player, Wall3):
                finish = 0
                window.blit(lose, (200,200))
                money_sound.play()
    if finish == 2:        
        window.blit(background,(0,0))
        player.reset()
        cyborg.reset()
        final.reset()
        Wall1.reset()
        Wall2.reset()
        Wall3.reset()
        Wall4.reset()
        nocllip_ind.reset()
        player.update()        
        cyborg.update()        
        
        if sprite.collide_rect(player, final):
            finish += 1
            window.blit(win, (200,200))
            money_sound.play()
            display.update()
            sleep(2.5)
            player.rect.x = 5
            player.rect.y = win_height - 80       
            
        if key.get_pressed()[K_n] and nocllip == 0:
            nocllip = 1
            nocllip_ind = Wall(5,5,10,10,(225,0,0))
        if key.get_pressed()[K_m] and nocllip == 1 :
            nocllip = 0
            nocllip_ind = Wall(5,5,10,10,(0,225,0))
        if nocllip == 0 :    
            if sprite.collide_rect(player, cyborg):
                finish = 0
                window.blit(lose, (200,200))
                kick_sound.play()

            if sprite.collide_rect(player, Wall1) or sprite.collide_rect(player, Wall2) or sprite.collide_rect(player, Wall3):
                finish = 0
                window.blit(lose, (200,200))
                money_sound.play()
    display.update()
    clock.tick(FPS)