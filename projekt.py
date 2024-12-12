import pygame as py
import random

SCREEN_WIDHT = 832
SCREEN_HEIGHT = 1000
x = 120
y = 700

py.init()

ekran = py.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])
zegar = py.time.Clock()
obraz_tla = py.image.load("background.png")
taksowka = py.image.load("TAXI.png")

gra_dziala = True

while gra_dziala:
    for zdarzenie in py.event.get():
            if zdarzenie.type == py.KEYDOWN:
                if zdarzenie.type == py.QUIT:
                    gra_dziala = False
                if zdarzenie.key == py.K_ESCAPE:
                    gra_dziala = False

                if x > 120:
                    if zdarzenie.key == py.K_a:
                         x -= 216
                
                if x < 548:
                    if zdarzenie.key == py.K_d:
                        x += 216

                        
    ekran.blit(obraz_tla, (0 , 0))
    ekran.blit(taksowka, (x , y))

    py.display.flip()

    zegar.tick(60)
