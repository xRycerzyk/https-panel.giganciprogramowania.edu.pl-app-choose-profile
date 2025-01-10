import pygame as py
import random
import time
from pygame.sprite import Group
from pygame import rect

class Auto1(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('car1.png')
        self.rect = self.image.get_rect(center = (180/2, 280/2))

class Taksowka(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('TAXI.png')
        self.rect = self.image.get_rect(center = (154/2, 280/2))

class Auto2(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load('car2.png')
        self.rect = self.image.get_rect(center = (180/2, 280/2))


SCREEN_WIDHT = 832
SCREEN_HEIGHT = 1000
x = 120
y = 700

x2 = 990
points = 0

py.init()

auto1_group = py.sprite.Group()
auto2_group = py.sprite.Group()

ekran = py.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])
zegar = py.time.Clock()
obraz_tla = py.image.load("background.png")
taksowka = Taksowka()
auto1 = Auto1()
PORUSZ_AUTEM = py.USEREVENT+1
py.time.set_timer(PORUSZ_AUTEM, 10)
auto2 = Auto2()

auto1_group.add(auto1)
auto2_group.add(auto2)

gra_dziala = True

#pozycja = x2, 0
y2 = -200
y3 = -200

x3 = random.randrange(120, 638 , 216)
x2 = random.randrange(120, 638 , 216)

while x2 == x3:
    x3 = random.randrange(120, 638 , 216)
    x2 = random.randrange(120, 638 , 216)

pozycja = x2, y2
pozycja1 = x3, y3

a = random.randint(8, 13)
b = random.randint(8, 13)

while gra_dziala:
    pozycja = x2, y2
    pozycja1 = x3, y3
    y2 += a
    y3 += b

    kolizja_z_autem1 = py.sprite.spritecollideany(taksowka, auto1_group)
    kolizja_z_autem2 = py.sprite.spritecollideany(taksowka, auto2_group)



    for zdarzenie in py.event.get():
        if zdarzenie.type == py.QUIT:
                gra_dziala = False

        if y2 >= 1000:
             x2 = random.randrange(120, 638 , 216)
             y2 = -600
             points += 1

             a = random.randint(8, 13)
             #b = random.randint(8, 13)
             
             while x3 == x2:
                 x2 = random.randrange(120, 638 , 216)
        
        if y3 >= 1000:
            x3 = random.randrange(120, 638 , 216)
            y3 = -600

            #a = random.randint(8, 13)
            b = random.randint(8, 13)

            while x3 == x2:
                 x3 = random.randrange(120, 638 , 216)
        
        if points >= 50:
            gra_dziala = False

        if kolizja_z_autem1 or kolizja_z_autem2:
            gra_dziala = False

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

time.sleep(1)
py.quit()
