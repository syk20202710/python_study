import pygame as pg
import sys
import random


pg.init()
screen = pg.display.set_mode((1000,400))

r1= pg.Rect(50,50,50,50)
r2= pg.Rect(200,50,50,50)

bg= pg.image.load('images/bg.png')
rr= pg.image.load('images/rr.png')
potion = pg.image.load('images/potion.png')
fire = pg.image.load('images/fire.png')
mob = pg.image.load('images/mob.png')
win = pg.image.load('images/win.png')


x= random.randint(500,650) #몹의 x축 등장 위치를 500~650에서 무작위로 결정
y= random.randint(0,50)   #몹의 y축 등장 위치를 0~50에서 무작위로 결정
r4 = pg.Rect(x,y,50,50) #몹의 이미지를 표시할 사각형 만들기

magic = False   #변수추가
fire_on = False # fire_on 변수를 False로 설정

#이동 부분을 함수로 구현
def move(r):
    if key[pg.K_RIGHT]:
        r.x = r.x +1
    
    if key[pg.K_LEFT]:
        r.x = r.x -1

    if key[pg.K_UP]:
        r.y = r.y -1

    if key[pg.K_DOWN]:
        r.y = r.y +1

pg.mixer
while True :
    screen.blit(bg, (0,0))
    key = pg.key.get_pressed()
    move(r1)
    screen.blit(rr,r1)

    if magic == True and r3.colliderect(r4):

        screen.blit(win,r4)
        pg.display.update()
        pg.time.delay(5500)
        pg.quit()
        sys.exit()
    
    screen.blit(mob,r4)
    r4.x = r4.x - 0.5  #몹의 위치를 왼쪽으로 0.5만큼 이동시키기
   

    if magic == False:
        screen.blit(potion,r2)
        if r1.colliderect(r2):
            magic = True
            r3 = pg.Rect(r1.x + 65, r1.y + 25, 50, 50)
    else:
        if key[pg.K_SPACE]:
            fire_on = True #fire_on 변수를 True로 설정
        screen.blit(fire,r3)
        if fire_on:
            r3.x = r3.x+1
        else:
            move(r3)
      

        
    pg.display.update()
        

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
