import pygame
import pygame as py
from py import rect
import copy
from py.sprite import Group


SCREEN_WIDHT = 832
SCREEN_HEIGHT = 1000
x2 = 
y2 = 

class Auto(py.sprite.Sprite)
    def __init__(self, x, y,):
        self.pozycja = py.Rect(x, y, 96, 48)
        self.auto = py.image.load('car1.png')

        def klon(self):
            self.auto_copy = copy.copy(self.auto)
        
        def maska(self):
            maska_auta = 0

            while True:
                maska_auta = (random.randint(1, 128), random.randint(1, 128), random.randint(1, 128)) 

            self.auto_copy.fill(maska_auta, special_flags=py.BLEND_ADD)

            

    
    
    







