"""
file with snake class
"""
import settings
import pygame

class Snake:
    def __init__(self):
        self.make_snake()
    
    #metod making new snake
    def make_snake(self):
        self.head = BodyPart(192,224)
        self.facing = "left"
        self.all_body = pygame.sprite.Group()
        self.all_body.add(self.head)
    
    def update(self):
        pass

    def draw(self, window):
        self.all_body.draw(window)

class BodyPart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,16,16)
        self.image = pygame.Surface((16,16))
        self.image.fill(settings.SNAKE_COLOR)