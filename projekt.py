import pygame as py
import random
import time
from pygame.sprite import Group
from pygame import rect

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
auto1 = py.image.load("car1.png")
PORUSZ_AUTEM = py.USEREVENT+1
py.time.set_timer(PORUSZ_AUTEM, 10)
auto2 = py .image.load("car2.png")

gra_dziala = True
#pozycja = x2, 0
y2 = -200
y3 = -200

x3 = random.randrange(120, 638 , 216)
x2 = random.randrange(120, 638 , 216)
pozycja = x2, y2
pozycja1 = x3, y3

while gra_dziala:
    pozycja = x2, y2
    pozycja1 = x3, y3
    y2 += 10
    y3 += 10

    for zdarzenie in py.event.get():
        if zdarzenie.type == py.QUIT:
                gra_dziala = False

        if y2 == 1000:
             x2 = random.randrange(120, 638 , 216)
             y2 = -200
        
        if y3 == 1000:
            x3 = random.randrange(120, 638 , 216)
            y3 = -200

        elif zdarzenie.type == py.KEYDOWN:
            if zdarzenie.key == py.K_ESCAPE:
                gra_dziala = False

            if x > 120:
                if zdarzenie.key == py.K_a:
                     x -= 108
                     x -= 108
                
            if x < 548:
                if zdarzenie.key == py.K_d:
                    x += 108
                    x += 108

    ekran.blit(obraz_tla, (0 , 0))
    ekran.blit(taksowka, (x , y))
    ekran.blit(auto1 , (pozycja))
    ekran.blit(auto2 , (pozycja1))

    py.display.flip()

    zegar.tick(360)
