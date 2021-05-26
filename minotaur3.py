import pygame
import os 
from enemy import Enemy

imgs = []

for x in range(18):


            imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur3/walking/Minotaur_03_Walking_"+ str(x) +".png")),(96, 64)))
        
class Minotaur3(Enemy):
     
    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health =5
        self.health = self.max_health
        self.imgs = imgs[:]
        