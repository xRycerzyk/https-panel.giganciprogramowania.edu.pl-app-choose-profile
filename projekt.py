import pygame as py
import random
import time
import copy
from Auto1 import Auto

SCREEN_WIDHT = 832
SCREEN_HEIGHT = 1000
x = 120
y = 700

x2 = 990

py.init()

ekran = py.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])
zegar = py.time.Clock()
obraz_tla = py.image.load("background.png")
taksowka = py.image.load("TAXI.png")
auto = 

gra_dziala = True

while gra_dziala:
    y2 =  random.randrange(120, 548, 216)
    for zdarzenie in py.event.get():
            if zdarzenie.type == py.QUIT:
                    gra_dziala = False
            elif zdarzenie.type == py.KEYDOWN:
                if zdarzenie.key == py.K_ESCAPE:
                    gra_dziala = False

                if x > 120:
                    if zdarzenie.key == py.K_a:
                         x -= 108
                         time.sleep(0.2)
                         x -= 108
                
                if x < 548:
                    if zdarzenie.key == py.K_d:
                        x += 108
                        time.sleep(0.2)
                        x += 108

                        
    ekran.blit(obraz_tla, (0 , 0))
    ekran.blit(taksowka, (x , y))
    ekran.blit(auto , (x2 , y2))

    py.display.flip()

    zegar.tick(60)
