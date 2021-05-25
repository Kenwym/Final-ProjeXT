import pygame
import os 
from enemy import Enemy



class Minotaur(Enemy):
     
    def __init__(self):
        super().__init__()
        self.health = 10
        self.imgs = []
        
        for x in range(18):


            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur/walking/Minotaur_01_Walking_"+ str(x) +".png")),(96, 64)))
        