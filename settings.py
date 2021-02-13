"""
file where are setting are stored
"""
import pygame

# game window size
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 416

# game framerate
FRAME_RATE = 60

# game elements colors
SNAKE_COLOR = (255, 255, 255)
APPLE_COLOR = (0, 200, 0)

# set game speed, less == faster and it has to be divisor of 60
GAME_SPEED = 10

# loadimages
PRESS = pygame.image.load("sprites/press_to_start.png")
GAME_OVER =  pygame.image.load("sprites/game_over.png")
BG = pygame.image.load("sprites/background.png")
NUMBERS = [
    pygame.image.load("sprites/0.png"),
    pygame.image.load("sprites/1.png"),
    pygame.image.load("sprites/2.png"),
    pygame.image.load("sprites/3.png"),
    pygame.image.load("sprites/4.png"),
    pygame.image.load("sprites/5.png"),
    pygame.image.load("sprites/6.png"),
    pygame.image.load("sprites/7.png"),
    pygame.image.load("sprites/8.png"),
    pygame.image.load("sprites/9.png"),
]