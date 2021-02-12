"""
file with game class
"""
import settings
import pygame
import sys

from pygame.locals import *

class Game:
    #init pygame module
    pygame.init()

    def __init__(self):
        #start game window
        self.window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.manage_input()
            pygame.display.update()
            self.clock.tick(settings.FRAME_RATE)

    #input managing method
    def manage_input(self):
        #loop thrugh income events
        for event in pygame.event.get():
            #if player exits window stop pygame module and close program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()