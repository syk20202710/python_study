import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((1000,400))


while True:
    #종료 버튼을누르면 종료시키는 코드
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
