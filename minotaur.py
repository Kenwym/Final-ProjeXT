import pygame
import os 
from enemy import Enemy

imgs = []

for x in range(18):


            imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur/walking/Minotaur_01_Walking_"+ str(x) +".png")),(96, 64)))
        
class Minotaur(Enemy):
     
    def __init__(self):
        super().__init__()
        self.max_health =1
        self.health = self.max_health
        self.imgs = imgs[:]
        self.money = 1
        self.name = "minotaur"