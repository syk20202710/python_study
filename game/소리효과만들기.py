import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1000,400))

bg = pg.image.load('images/bg.png')
rr=pg.image.load('images/rr.png')
x=0
y=0

while True:
    key = pg.key.get_pressed()
    if key[pg.K_RIGHT] :    #오른쪽 화살표를 눌렀을 때
        pg.mixer.Sound('sounds/powerup.wav').play() #powerup.wav 소리 재생
        
    elif key[pg.K_LEFT] : #왼쪽 화살표
        pg.mixer.Sound('sounds/powerup2.wav').play()
    elif key[pg.K_UP] :   #위쪽 화살표
        pg.mixer.Sound('sounds/fire.wav').play()
    elif key[pg.K_DOWN] :   # 아래쪽 화살표
        pg.mixer.Sound('sounds/stage_clear.wav').play()
    screen.blit(bg, (x,y))
    pg.display.update()
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
        
