import pygame
import os




class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    
    
    def click(self, X, Y):
        
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self,win):
        win.blit(self.img, (self.x, self.y))



class Menu:
    
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_names = []
        self.buttons = []
        self.items = 0
        self.bg = img
        
    def click(self, X, Y):
        
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def add_btn(self, img, name):
        self.items += 1
        
        inc_x = self.width/self.items
        btn_x = self.items * inc_x - img.get_width()/2
        btn_y = self.y + self.height/2 - img.get_height()/2
        self.buttons.append(Button(btn_x, btn_y, img, name))


    def draw(self, win):
        
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y))
        for item in self.buttons:
            item.draw(win)

    def get_clicked(self, X, Y):
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name
        
        
        
        
        
        
        
        