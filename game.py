import pygame
from pygame.locals import *
import os
from minotaur import Minotaur
from minotaur2 import Minotaur2
from minotaur3 import Minotaur3
from bomber import Bomber


class Game():
    
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.towers = [Bomber(640,280)]
        self.enemy = [Minotaur()]
        self.money = 100
        self.lives = 10
        self.bg = pygame.image.load("assets/bg1.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(30)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                
            to_del= []
            for en in self.enemy:
                if en.x >= 1270:
                    to_del.append(en)
                    
            for f in to_del:
                self.enemy.remove(f)
                    
            self.draw()
        pygame.quit()
        
    def draw(self):
        self.win.blit(self.bg, (0,0))
        
        for en in self.enemy:
            en.draw(self.win)
            
        for to in self.towers:
            to.draw(self.win)
        
            
        pygame.display.update()
g = Game()
g.run()