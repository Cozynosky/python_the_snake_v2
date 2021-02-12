"""
file with game class
"""
import settings
import snake
import pygame
import sys

from pygame.locals import *

class Game:
    #init pygame module
    pygame.init()

    def __init__(self):
        #start game window
        self.window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        #create game clock
        self.clock = pygame.time.Clock()
        #flag with game stance
        self.game_on = False
        #make new snake
        self.snk = snake.Snake()

    #methon with main game loop
    def run(self):
        while True:
            self.manage_input()
            #run game only when game playing flag is set True
            if self.game_on:
                self.update()
                self.draw()
            #update the screen and wait for proper framerate
            pygame.display.update()
            self.clock.tick(settings.FRAME_RATE)

    def update(self):
        self.snk.update()
    
    def draw(self):
        self.window.fill(settings.BG_COLOR)
        self.snk.draw(self.window)

    #input managing method
    def manage_input(self):
        #loop thrugh income events
        for event in pygame.event.get():
            #if player exits window stop pygame module and close program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #manage keyup events
            if event.type == KEYUP:
                #change game stance to True if it is False
                if not self.game_on:
                    self.game_on = True 