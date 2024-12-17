import pygame
import pygame as py
import random
from pygame import rect
import copy
from pygame.sprite import Group

class Auto(py.sprite.Sprite):
    
    SCREEN_WIDHT = 832
    SCREEN_HEIGHT = 1000
    x2 = 990
    y2 = random.randint()

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
