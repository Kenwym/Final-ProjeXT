import pygame
import os 
from enemy import Enemy

imgs = []

for x in range(18):


            imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur2/walking/Minotaur_02_Walking_"+ str(x) +".png")),(96, 64)))
        
class Minotaur2(Enemy):
     
    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health =3
        self.health = self.max_health
        self.imgs = imgs[:]