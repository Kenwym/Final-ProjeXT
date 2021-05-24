import pygame
import os 
from enemy import Enemy



class Minotaur2(Enemy):
    
        
    def __init__(self):
        super().__init__()
        self.health = 40
        self.imgs = []
        
        for x in range(18):

        
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur2/walking/Minotaur_02_Walking_"+ str(x) +".png")),(64, 64)))
        
        
        
        