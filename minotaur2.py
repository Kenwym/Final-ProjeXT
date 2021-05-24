import pygame
import os 
from enemy import Enemy



class Minotaur2(Enemy):
    imgs = []
    
    for x in range(18):
        add_str = str(x)
        
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/enemy/minotaur2/walking/Minotaur_02_Walking_"+ add_str +".png")),(64, 64)))
        
        
    def __init__(self):
        super().__init__()
        self.health = 40