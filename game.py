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
        #varviable to control snake speed
        self.ticks = 0
        #flag with game stance
        self.game_on = False
        #make new snake
        self.snk = snake.Snake()

    #method with main game loop
    def run(self):
        self.draw()
        while True:
            self.manage_input()
            #run game only when game playing flag is set True
            if self.game_on and self.ticks % settings.GAME_SPEED == 0:
                self.update()
                self.draw()
                self.ticks = 0
            self.ticks += 1
            #update the screen and wait for proper framerate
            pygame.display.update()
            self.clock.tick(settings.FRAME_RATE)

    #update objects positions
    def update(self):
        self.snk.update()
    
    #draw game elements on the screen
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
            elif event.type == KEYUP:
                #change game stance to True if it is False
                if not self.game_on:
                    self.game_on = True
            elif event.type == KEYDOWN:
                if (event.key == K_a or event.key == K_LEFT) and self.snk.facing != "right":
                    self.snk.facing = "left"
                elif (event.key == K_d or event.key == K_RIGHT) and self.snk.facing != 'left':
                    self.snk.facing = "right"
                elif (event.key == K_w or event.key == K_UP) and self.snk.facing != 'down':
                    self.snk.facing = "up"
                elif (event.key == K_s or event.key == K_DOWN) and self.snk.facing != 'up':
                    self.snk.facing = "down"