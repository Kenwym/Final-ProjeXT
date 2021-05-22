import pygame
from pygame.locals import *
import os
from minotaur import Minotaur

class Game():
    
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))

        self.towers = []

        self.enemy = [Minotaur()]
        self.money = 100
        self.lives = 10
        self.bg = pygame.image.load("assets/Menu_Building.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []


    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(60)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                
            to_del= []
            for en in self.enemy:
                if en.x < 1000:
                    to_del.append(en)
                    
            for f in to_del:
                self.enemy.remove(f)
                    
                
                    
            self.draw()
            
        pygame.quit()
        
    def draw(self):
        self.win.blit(self.bg, (0,0))
        
        for en in self.enemy:
            en.draw(self.win)
        
            
        pygame.display.update()
g = Game()
g.run()