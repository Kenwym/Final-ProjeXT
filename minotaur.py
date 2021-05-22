import pygame
import os 
from ennemy import Enemy



class Minotaur(Enemy):
    imgs = []
    
    for x in range(18):
        add_str = str(x)
        
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/minotaur/walking/Minotaur_01_Walking_"+ add_str +".png")),(64, 64)))
        
        
    def __init__(self):
        super().__init__
        self.animation_count = 0
        self.path = [(134, 179),(228, 183),(395, 186),(581, 193),(730, 192),(855, 210),(887, 301),(877, 501),(803, 529)
                     ,(650, 384),(517, 365),(380, 464),(267, 539),(190, 451),(97, 420),(37, 420)]
        self.path_pos = 0
        self.dis = 0
        self.move_count = 0
        self.move_dis = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]
