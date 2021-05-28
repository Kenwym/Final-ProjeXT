import pygame
import os
from pygame.locals import *
from minotaur import Minotaur
from minotaur2 import Minotaur2
from minotaur3 import Minotaur3
from bomber import Bomber
from stonebomber import StoneBomber
from firebomber import FireBomber
from menu import VerticalMenu, PlayPauseButton
import time
import random

pygame.font.init()
pygame.init()

lives_img = pygame.transform.scale(pygame.image.load(os.path.join("assets/lives.png")), (32, 32))
star_img =  pygame.transform.scale(pygame.image.load(os.path.join("assets/money.png")), (32, 32))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("assets/side.png")), (120, 390))

buy_bomb = pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/buy_bomb.png")), (75, 75))
buy_stone =pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/buy_stone.png")), (75, 75))
buy_fire = pygame.transform.scale(pygame.image.load(os.path.join("assets/defense/buy_fire.png")), (75, 75))

play_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets/button_play.png")), (75, 75))
pause_btn = pygame.transform.scale(pygame.image.load(os.path.join("assets/button_pause.png")), (75, 75))

wave_bg = pygame.transform.scale(pygame.image.load(os.path.join("assets/wave_bg.png")), (225, 75))

bomber_name = ["bomber"]
stonebomber_name = ["stonebomber"]
firebomber_name = ["firebomber"]
waves = [
    [20, 0, 0],
    [50, 0, 0],
    [100, 0, 0],
    [0, 20, 0],
    [0, 50, 0],
    [0, 100, 0],
    [20, 100, 0],
    [50, 100, 0],
    [100, 100, 0],
    [0, 50, 3],
    [20, 0, 100],
    [20, 0, 150],
    [200, 100, 200]]

class Game():  
    def __init__(self):
        self.width = 1209
        self.height = 713
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bomb_towers  = []
        self.stone_towers = []
        self.fire_towers  = []
        self.enemys = []
        self.lives = 10
        self.money = 2000
        self.bg = pygame.image.load("assets/MAPE.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 250, side_img)
        self.menu.add_btn(buy_bomb, "buy_bomb", 500)
        self.menu.add_btn(buy_stone, "buy_stone", 750)
        self.menu.add_btn(buy_fire, "buy_fire", 1000)
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = True
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, 10, self.height - 85)
    
    def gen_enemies(self):
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
                self.pause = True
                self.playPauseButton.paused = self.pause
        else:
            wave_enemies = [Minotaur(), Minotaur2(), Minotaur3()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break
    
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            if self.pause == False:    
                if time.time() - self.timer >= random.randrange(1,6)/3:
                        self.timer = time.time()
                        self.gen_enemies()
            pos = pygame.mouse.get_pos()
            
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.bomb_towers[:] + self.stone_towers[:] + self.fire_towers[:] 
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.bomb_towers[:] + self.stone_towers[:] + self.fire_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in bomber_name:
                                self.bomb_towers.append(self.moving_object)
                            elif self.moving_object.name in stonebomber_name:
                                self.stone_towers.append(self.moving_object)
                            elif self.moving_object.name in firebomber_name:
                                self.fire_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        if self.playPauseButton.click(pos[0], pos[1]):
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                       
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()

                        if not(btn_clicked):
                            for tw in self.bomb_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            for tw in self.stone_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False
                            
                            for tw in self.fire_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

            # loop through enemies
            if not self.pause:
                to_del = []
                for en in self.enemys:
                    en.move()
                    if en.x >480 and en.y > 542 :
                        to_del.append(en)

                # delete all enemies off the screen
                for d in to_del:
                    self.lives -= 1
                    self.enemys.remove(d)

                
                for tw in self.bomb_towers:
                    self.money += tw.attack(self.enemys)
                for tw in self.stone_towers:
                    self.money += tw.attack(self.enemys)
                for tw in self.fire_towers:
                    self.money += tw.attack(self.enemys)

                # if you lose
                if self.lives <= 0:
                    print("You Lose")
                    run = False

            self.draw()
            
                
                
                        
                
        pygame.quit()
        
    def point_to_line(self, tower):
        return True
    
    def draw(self):
        self.win.blit(self.bg, (0,0))

        # draw placement rings
        if self.moving_object:
            for tower in self.bomb_towers:
                tower.draw_placement(self.win)

            for tower in self.stone_towers:
                tower.draw_placement(self.win)
            
            for tower in self.fire_towers:
                tower.draw_placement(self.win)
            
            self.moving_object.draw_placement(self.win)

        # draw bomb towers
        for tw in self.bomb_towers:
            tw.draw(self.win)

        # draw stone towers
        for tw in self.stone_towers:
            tw.draw(self.win)
        
        # draw fire towers
        for tw in self.fire_towers:
            tw.draw(self.win)
                
        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        self.menu.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)


        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = pygame.transform.scale(lives_img,(50,50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(star_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        # draw wave
        self.win.blit(wave_bg, (1000,600))
        text = self.life_font.render("Wave " + str(self.wave+1), 1, (255,255,255))
        self.win.blit(text, (1017,619))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_bomb", "buy_stone","buy_fire"]
        object_list = [Bomber(x,y), StoneBomber(x,y), FireBomber(x,y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")
        
            
        pygame.display.update()
g = Game()
g.run()