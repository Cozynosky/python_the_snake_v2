"""
file where are setting are stored
"""
import pygame

#game window size
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 416

#game framerate
FRAME_RATE = 60

#game elements colors
SNAKE_COLOR = (255,255,255)
APPLE_COLOR = (0,200,0)

#set game speed, less == faster and it has to be divisor of 60
GAME_SPEED = 10

#loadimages
BG = pygame.image.load("sprites/background.png")