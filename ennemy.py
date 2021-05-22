import pygame
from pygame.locals import *
import os
import math

class Enemy:
    imgs = []
    def __init__(self):
        super().__init__()
        
        self.width = 64
        self.height = 64
        self.health = 10
        self.vel = 3
        self.animation_count = 0
        self.img = None
        self.path = [(134, 179),(228, 183),(395, 186),(581, 193),(730, 192),(855, 210),(887, 301),(877, 501),(803, 529)
                     ,(650, 384),(517, 365),(380, 464),(267, 539),(190, 451),(97, 420),(37, 420)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        
    def draw(self,win):
        
        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1
        if self.animation_count > len(self.imgs)*3:
            self.animation_count = 0
            win.blit(self.img, (self.x, self.y))
        self.move()
        
        
    def collide(self, X, Y):
        
        if X <= self.x + self.width and X >= self.x:
            
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False
    
    
    def move(self):
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2,y2 = (-10, 156)
        else:
            
            x2,y2= self.path[self.path_pos+1]
        
        
        self.move_dis += math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        
        self.move_count += 1
        dirn = (x2 - x1, y2 - y1)
        
        move_x, move_y = (self.x + dirn[0]* self.move_count, self.y + dirn[1]* self.move_count)
        
        self.dis += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)
        
        if self.dis >= self.move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False
            
        self.x = move_x
        self.y = move_y
        return True
            
    def hit(self):
        self.health -=1
        if self.health <= 0:
            return True

