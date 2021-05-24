import pygame
from pygame.locals import *
import os
import math

class Enemy:
    imgs = []
    def __init__(self):
        
        self.width = 64
        self.height = 64
        self.health = 10
        self.vel = 1
        self.health = 1
        self.animation_count = 0
        self.img = None
        self.path = [(-30,480),(5, 480), (405, 485), (495, 450), (526, 371), (535, 271), (624, 234), (702, 244), (750, 296), (779, 374), (860, 409), (972, 412), (1041, 445), (1129, 483), (1280, 488)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.flipped = False
        
    def draw(self,win):
        
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 15))
        self.move()
        
        
    def collide(self, X, Y):
        
        if X <= self.x + self.width and X >= self.x:
            
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False
    
    
    def move(self):
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        if dirn[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        if dirn[0] >= 0: 
            if dirn[1] >= 0: 
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: 
            if dirn[1] >= 0:  
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            
    def hit(self):
        self.health -=1
        if self.health <= 0:
            return True

