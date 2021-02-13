"""
file with game class
"""
import settings
import apple
import snake
import pygame
import sys

from pygame.locals import *


class Game:
    # init pygame module
    pygame.init()

    def __init__(self):
        # start game window
        self.window = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        # create game clock
        self.clock = pygame.time.Clock()
        # create new game
        self.new_game()

    # method with main game loop
    def run(self):
        self.draw()
        while True:
            self.manage_input()
            if not self.game_on:
                rect = settings.PRESS.get_rect()
                rect.center = self.window.get_rect().center
                self.window.blit(settings.PRESS,rect)
            # run game only when game playing flag is set True
            if self.game_on and self.ticks % settings.GAME_SPEED == 0:
                self.update()
                self.draw()
                self.ticks = 0
                self.time_since_change = 10
            self.ticks += 1
            self.time_since_change += 1
            # update the screen and wait for proper framerate
            pygame.display.update()
            self.clock.tick(settings.FRAME_RATE)

    # make new game method
    def new_game(self):
        # varaible to store our score
        self.score = 0
        # variable to control snake speed
        self.ticks = 0
        # flag with game stance
        self.game_on = False
        # store ticks since last facing change to avoid bugs
        self.time_since_change = 0
        # make new snake
        self.snk = snake.Snake()
        # make new apple
        self.appl = apple.Apple(self.snk)

    # update objects positions
    def update(self):
        self.snk.update()
        # check if snake collided with wall, if true end active game and reset snake, show game over info and wait some time
        if self.snk.wall_collision() or self.snk.self_collision():
            self.new_game()
            rect = settings.GAME_OVER.get_rect()
            rect.center = self.window.get_rect().center
            self.window.blit(settings.GAME_OVER,rect)
            pygame.display.update()
            pygame.time.delay(700)
        elif self.snk.apple_collision(self.appl):
            self.score += 1
            self.appl = apple.Apple(self.snk)
            # make snake grow up
            self.snk.grow = True

    # draw game elements on the screen
    def draw(self):
        self.window.blit(settings.BG, (0, 0))
        self.appl.draw(self.window)
        self.snk.draw(self.window)
        self.draw_score()

    # special met to draw score
    def draw_score(self):
        s_scr = str(self.score)
        surface = pygame.Surface((21 * len(s_scr),27))
        for i in range(len(s_scr)):
            surface.blit(settings.NUMBERS[int(s_scr[i])],(16*i,0))
        rect = surface.get_rect()
        rect.topleft = (150,38)
        self.window.blit(surface,rect)

    # input managing method
    def manage_input(self):
        # loop thrugh income events
        for event in pygame.event.get():
            # if player exits window stop pygame module and close program
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # manage keyup events
            elif event.type == KEYUP:
                # change game stance to True if it is False
                if not self.game_on:
                    self.game_on = True
            elif event.type == KEYDOWN:
                # manage changing direction only when snake is ready, otherway we could go backwards
                if self.time_since_change >= settings.GAME_SPEED:
                    if (
                        event.key == K_a or event.key == K_LEFT
                    ) and self.snk.facing != "right":
                        self.snk.facing = "left"
                        self.time_since_change = 0
                    elif (
                        event.key == K_d or event.key == K_RIGHT
                    ) and self.snk.facing != "left":
                        self.snk.facing = "right"
                        self.time_since_change = 0
                    elif (
                        event.key == K_w or event.key == K_UP
                    ) and self.snk.facing != "down":
                        self.snk.facing = "up"
                        self.time_since_change = 0
                    elif (
                        event.key == K_s or event.key == K_DOWN
                    ) and self.snk.facing != "up":
                        self.snk.facing = "down"
                        self.time_since_change = 0
