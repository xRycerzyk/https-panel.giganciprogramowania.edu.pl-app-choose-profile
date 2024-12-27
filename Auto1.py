import pygame
import pygame as py
import random
from pygame import rect
import copy
from pygame.sprite import Group

class Auto(py.sprite.Sprite):
    
    SCREEN_WIDHT = 832
    SCREEN_HEIGHT = 1000

    def __init__(self, x, y,):
        super().__self__()
        self.rect = py.Rect(x, y, 96, 48)
        self.image = py.image.load("car1.png")
        self.auto_copy = self.image.copy()

    def klon(self):
            self.auto_copy = copy.copy(self.auto)
        
    def maska(self):
        maska_auta = (random.randrange(1, 128), random.randrange(1, 128), random.randrange(1, 128)) 

        self.auto_copy.fill(maska_auta , special_flags=py.BLEND_ADD)
