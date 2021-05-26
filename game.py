import pygame
from pygame.locals import *
import os
from minotaur import Minotaur
from minotaur2 import Minotaur2
from minotaur3 import Minotaur3
from bomber import Bomber1
import time
import random
class Game():
    
    def __init__(self):
        self.width = 1209
        self.height = 713
        self.win = pygame.display.set_mode((self.width, self.height))
        self.towers = [Bomber1(363, 228)]
        self.enemies = []
        self.money = 100
        self.lives = 10
        self.bg = pygame.image.load("assets/MAPE.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.selected_tower = None
        self.timer = time.time()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        
        while run:
            
            if time.time() - self.timer >=2:
                self.timer = time.time()
                self.enemies.append(random.choice([Minotaur(),Minotaur2(),Minotaur3()]))
            
            clock.tick(30)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for tw in self.towers:
                        if tw.click(pos[0], pos[1]):
                            tw.selected = True
                            self.selected_tower = tw
                        else:
                            tw.selected = False
                
            to_del= []
            for en in self.enemies:
                if en.x > 480 and en.y > 542:
                    to_del.append(en)
                    
            for f in to_del:
                self.enemies.remove(f)
                
            for tw in self.towers:
                tw.attack(self.enemies)
            
                    
            self.draw()
        pygame.quit()
        
    def draw(self):
        self.win.blit(self.bg, (0,0))
        
        for en in self.enemies:
            en.draw(self.win)
            
        for tw in self.towers:
            tw.draw(self.win)
        
            
        pygame.display.update()
g = Game()
g.run()