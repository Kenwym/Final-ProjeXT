import pygame
from menu import Menu
import os
import math
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("assets/menu_tower.png")), (150, 75))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets/upgrade.png")), (50, 50))
class Tower:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.level = 0
        self.selected = False
        self.imgs = []
        
        self.menu = Menu(self, self.x, self.y, menu_bg, [125, 150, 'MAX'])
        self.menu.add_btn(upgrade_btn, "Upgrade")

        self.tower_imgs = []
        self.place_color = (0,0,255, 100)

    def draw(self,win):
        
        img = self.tower_imgs[self.level]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2-45))
    
        if self.selected:
            self.menu.draw(win)
    
    
    def draw_radius(self,win):
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x - self.range, self.y - self.range))
     
    def draw_placement(self,win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))
            
    def click(self, X, Y):
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        return self.sell_price[self.level-1]
    
    def upgrade(self):
        self.level += 1
        self.damage = int(self.damage *1.5)
        
    def get_upgrade_cost(self):
        return self.price[self.level]
    
    def move(self, x, y):
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()
    
    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True