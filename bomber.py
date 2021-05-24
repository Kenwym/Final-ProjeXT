import pygame
import os
from tower import Tower


class Bomber(Tower):
    
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.bomber_imgs = []
        self.bomb_count = 0
        
        
        for x in range(3):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/tower1/tower1_"+ str(x) +".png")),(64, 64)))
        
        for x in range(18,22):
            self.bomber_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/tower1/"+ str(x) +".png")),(32, 32)))
        
        
        
        
        
    def draw(self,win):
        super().draw(win)
        
        if self.bomb_count >= len(self.bomber_imgs)*10:
            self.bomb_count = 0
            
        
        
        bomber = self.bomber_imgs[self.bomb_count//10]
        win.blit(bomber,((self.x +self.width/2)- (bomber.get_width()/2), (self.y -bomber.get_height() )))
        self.bomb_count += 1
        
    def attack(self, enemy):
        pass
        
        