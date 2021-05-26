import pygame
import os
from tower import Tower
import math
import time


tower_imgs1 = []
bomb_imgs = []
bomb_imgs2 = []
bomb_imgs3 = []
for x in range(0,3):
    tower_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("assets/defense/tower1/tower1_"+str(x)+".png")),(96, 96)))

for a in range(10):
    bomb_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/tower1/tower3_1_00" + str(a)+ ".png")),(96,96)))
for b in range(10):
    bomb_imgs2.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/tower1/tower3_2_00" + str(b)+ ".png")),(96,96)))
    
for c in range(10):
    bomb_imgs3.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/tower1/tower3_3_00" + str(c)+ ".png")),(96,96)))
    
class Bomber1(Tower):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.bomb_imgs = bomb_imgs[:]
        self.bomb_count = 0
        self.range = 150
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 96
        self.moving = False
        self.name = "bomber1"
        self.timer= time.time()
        
    
    
    def draw(self,win):
        super().draw(win)
        super().draw_radius(win)
        if self.inRange and not self.moving:
            self.bomb_count += 1
            if self.bomb_count >= len(self.bomb_imgs):
                self.bomb_count = 0
        else:
            self.bomb_count = 0

        bomb = self.bomb_imgs[self.bomb_count ]
        
        win.blit(bomb, (self.x - bomb.get_width()/2, self.y - bomb.get_height()/2))

        
        
    
    def change_range(self,r):
        self.range = r
        
    def attack(self, enemies):
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y
            
            dis = math.sqrt((self.x - x)**2 +(self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)        
        enemy_closest.sort(key= lambda x: x.x)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >=1.8:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)
            

        

        
        