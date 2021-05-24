import pygame

class Tower:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.imgs = []
        
    def draw(self,win):
        
        img = self.tower_imgs[self.level]
        win.blit(img, (self.x-img.get_width()/2, self.y-img.get_height()/2))
    
    def click(self, X, Y):
        
        if X <= self.x + self.width and X >= self.x:
            
            if Y <= self.y + self.width and Y >= self.y:
                return True
        return False
    
    
    def sell(self):
        return self.sell_price[self.level-1]
    
    def upgrade(self):
        self.level += 1
    
    def get_upgrade_cost(self):
        return self.price[self.level-1]
    
        
    def move(self,x,y):
        self.x = x
        self.y = y
        