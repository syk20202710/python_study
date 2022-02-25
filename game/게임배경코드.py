import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1000,400))

bg= pg.image.load('images/bg.png') #하늘 배경
rr= pg.image.load('images/rr.png') #룡룡이 이미지

x=20
y=20
magic = False # 불투명/반투명 변수

while True:
    screen.blit(bg, (0,0))
    screen.blit(rr, (x,y)) #룡룡이 이미지를 화면에 나타내

    key =pg.key.get_pressed()
    
    if key[pg.K_RIGHT]:
        x=x+1
        
    if key[pg.K_LEFT]:
        x=x-1
        
    if key[pg.K_UP]:
        y=y-1
        
    if key[pg.K_DOWN]:
        y=y+1

        
    if key[pg.K_RETURN]:
        if magic == False :
            rr.set_alpha(100)
            magic =True

        else:
            rr.set_alpha(255)
            magic = False
        
    pg.display.update()

    for event in pg.event.get() :
       if event.type == pg.QUIT :
           pg.quit()
           sys.exit()
