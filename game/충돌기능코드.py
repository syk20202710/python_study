import pygame as pg
import sys


pg.init()
screen = pg.display.set_mode((1000,400))

r1= pg.Rect(50,50,40,50)
r2= pg.Rect(200,50,40,50)
bg= pg.image.load('images/bg.png')
rr= pg.image.load('images/rr.png')
potion = pg.image.load("images/potion.png")
magic = False   #변수추가

while True :
    screen.blit(bg, (0,0))

    key = pg.key.get_pressed()
    if key[pg.K_RIGHT]:
        r1.x = r1.x +1

    if key[pg.K_LEFT]:
        r1.x = r1.x -1

    if key[pg.K_UP]:
        r1.y = r1.y-1

    if key[pg.K_DOWN]:
        r1.y = r1.y +1

    if magic == False:
        screen.blit(potion,r2)
    if r1.colliderect(r2):
        magic = True
        rr.set_alpha(100)
        
            
    screen.blit(rr,r1)
  
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
