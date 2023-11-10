from pygame import *

#створи вікно гри

window = display.set_mode((700,500))

img = image.load("background.png")
background = transform.scale(img, (700,500))

clock = time.Clock()
FPS = 60
SPEED =10

sprite1 = transform.scale(image.load("sprite1.png"), (100,100))
sprite2 = transform.scale(image.load("sprite2.png"), (100,100))

x1=200
y1=200

x2=300
y2=300


game=True

while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    display.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 0:
        x1 = x1-SPEED
    if keys_pressed[K_UP] and y1 > 0:
        y1 = y1-SPEED
    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 = x1+SPEED
    if keys_pressed[K_DOWN] and y1 < 400:
        y1 = y1+SPEED

    if keys_pressed[K_a] and x2 > 0:
        x2 = x2-SPEED
    if keys_pressed[K_w] and y2 > 0:
        y2 = y2-SPEED
    if keys_pressed[K_d] and x2 < 600:
        x2 = x2+SPEED
    if keys_pressed[K_s] and y2 < 400:
        y2 = y2+SPEED


    clock.tick(FPS)
#задай фон сцени

#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»