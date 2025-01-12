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
points = 0

py.init()



ekran = py.display.set_mode([SCREEN_WIDHT, SCREEN_HEIGHT])
zegar = py.time.Clock()
obraz_tla = py.image.load("background.png")

PORUSZ_AUTEM = py.USEREVENT+1
py.time.set_timer(PORUSZ_AUTEM, 10)






gra_dziala = True

#pozycja = x2, 0
y2 = -200
y3 = -200


x3 = random.randrange(120, 638 , 216)
x2 = random.randrange(120, 638 , 216)

class Auto1():
    def __init__(self):
        global x2
        self.x2 = x2
        global y2
        self.y2 = y2
        self.hitbox = py.Rect(self.x2, self.y2, 180, 280)
        self.image = py.image.load('car1.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x2 , self.y2)
    
class Taksowka():
    def __init__(self):
        global x
        self.x = x
        global y
        self.y = y
        self.hitbox = py.Rect(self.x, self.y, 155, 281)
        self.image = py.image.load('TAXI.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x , self.y)

class Auto2():
    def __init__(self):
        global x3
        global y3
        self.x3 = x3
        self.y3 = y3
        self.hitbox = py.Rect(self.x3, self.y3, 180, 280)
        self.image = py.image.load('car2.png')
    
    def update_hitbox(self):
        self.hitbox.topleft = (self.x3 , self.y3)

taksowka = Taksowka()
auto1 = Auto1()
auto2 = Auto2()

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

    auto1.update_hitbox()
    taksowka.update_hitbox()
    auto2.update_hitbox()
        

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
            
             auto1.update_hitbox()
             taksowka.update_hitbox()
             auto2.update_hitbox()
        
        if y3 >= 1000:
            x3 = random.randrange(120, 638 , 216)
            y3 = -600

            #a = random.randint(8, 13)
            b = random.randint(8, 13)

            while x3 == x2:
                 x3 = random.randrange(120, 638 , 216)
            
            auto1.update_hitbox()
            taksowka.update_hitbox()
            auto2.update_hitbox()
        
        if points >= 50:
            gra_dziala = False

        elif zdarzenie.type == py.KEYDOWN:
            if zdarzenie.key == py.K_ESCAPE:
                gra_dziala = False
                

            if x > 120:
                if zdarzenie.key == py.K_a:
                     x -= 108
                     x -= 108

                auto1.update_hitbox()
                taksowka.update_hitbox()
                auto2.update_hitbox()
                
            if x < 548:
                if zdarzenie.key == py.K_d:
                    x += 108
                    x += 108
                
                auto1.update_hitbox()
                taksowka.update_hitbox()
                auto2.update_hitbox()

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
