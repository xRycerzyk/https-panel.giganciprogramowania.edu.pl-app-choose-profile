import pygame as py
import random
import time
from pygame.sprite import Group
from pygame import rect

SCREEN_WIDHT = 832
SCREEN_HEIGHT = 1000


py.init()

ekran = py.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])
zegar = py.time.Clock()
py.display.set_caption('Turbo Taxi Driver')
obraz_tla = py.image.load("background.png")

PORUSZ_AUTEM = py.USEREVENT+1
py.time.set_timer(PORUSZ_AUTEM, 10)

gra_dziala = True

class Auto1():
    def __init__(self):
        self.x = 990
        self.y = -200
        self.hitbox = py.Rect(self.x, self.y, 180, 280)
        self.image = py.image.load('car1.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x , self.y)
    
class Taksowka():
    def __init__(self):
        self.x = 120
        self.y = 700
        self.hitbox = py.Rect(self.x, self.y, 155, 281)
        self.image = py.image.load('TAXI.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x , self.y)

class Auto2():
    def __init__(self):
        self.x = 990
        self.y = -200
        self.hitbox = py.Rect(self.x, self.y , 180, 280)
        self.image = py.image.load('car2.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x , self.y)



taksowka = Taksowka()
auto1 = Auto1()
auto2 = Auto2()

auto1.y = -200
auto2.y = -200

auto2.x = random.randrange(120, 638 , 216)
auto1.x = random.randrange(120, 638 , 216)

taksowka.x = 120
taksowka.y = 700

auto1.x = 990
points = 0

while auto1.x == auto2.x:
    auto1.x = random.randrange(120, 638 , 216)
    auto2.x = random.randrange(120, 638 , 216)

#pozycja = auto1.x, auto1.y
#pozycja1 = x3, y3

a = random.randint(8, 13)
b = random.randint(8, 13)

while gra_dziala:

    prev_x = taksowka.x

    auto1.y += a
    auto2.y += b

    auto1.update_hitbox()
    taksowka.update_hitbox()
    auto2.update_hitbox()
        

    for zdarzenie in py.event.get():
        if zdarzenie.type == py.QUIT:
                gra_dziala = False

        if auto1.y >= 1000:
             auto1.x = random.randrange(120, 638 , 216)
             auto1.y = -600
             points += 1

             a = random.randint(8, 13)
             #b = random.randint(8, 13)
             
             while auto2.x == auto1.x:
                auto1.x = random.randrange(120, 638 , 216)
            
             auto1.update_hitbox()
             taksowka.update_hitbox()
             auto2.update_hitbox()
        
        if auto2.y >= 1000:
            auto2.x = random.randrange(120, 638 , 216)
            auto2.y = -600

            #a = random.randint(8, 13)
            b = random.randint(8, 13)

            while auto2.x == auto1.x:
                 auto2.x = random.randrange(120, 638 , 216)
            
            auto1.update_hitbox()
            taksowka.update_hitbox()
            auto2.update_hitbox()
        
        if points >= 50:
            gra_dziala = False

        elif zdarzenie.type == py.KEYDOWN:
            if zdarzenie.key == py.K_ESCAPE:
                gra_dziala = False
                

            if taksowka.x > 120:
                if zdarzenie.key == py.K_a:
                     taksowka.x -= 108
                     taksowka.x -= 108

                auto1.update_hitbox()
                taksowka.update_hitbox()
                auto2.update_hitbox()
                
            if taksowka.x < 548:
                if zdarzenie.key == py.K_d:
                    taksowka.x += 108
                    taksowka.x += 108
                
                auto1.update_hitbox()
                taksowka.update_hitbox()
                auto2.update_hitbox()
    
    if taksowka.hitbox.colliderect(auto1.hitbox):
        taksowka.x = prev_x
        gra_dziala = False
    if taksowka.hitbox.colliderect(auto2.hitbox):
        taksowka.x = prev_x
        gra_dziala = False

    ekran.blit(obraz_tla, (0 , 0))
    ekran.blit(taksowka.image, (taksowka.hitbox))
    ekran.blit(auto1.image, (auto1.hitbox))
    ekran.blit(auto2.image, (auto2.hitbox))

    auto1.update_hitbox()
    taksowka.update_hitbox()
    auto2.update_hitbox()

    py.display.flip()

    zegar.tick(360)

time.sleep(1)
py.quit()
