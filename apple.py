"""
file with apple class
"""
import settings
import random
import pygame

class Apple(pygame.sprite.Sprite):
    def __init__(self,snake):
        pygame.sprite.Sprite.__init__(self)
        self.make_apple(snake)
    
    #make new apple, coords have to be 16 multiple because of the game grid
    def make_apple(self,snake):
        x = random.randint(2,23) * 16
        y = random.randint(5,27) * 16
        self.rect = pygame.Rect(x,y,16,16)
        self.image = pygame.Surface((16,16))
        self.image.fill(settings.APPLE_COLOR)
        #if new apple spawned on collision make new one
        if snake.head.rect.colliderect(self.rect) or pygame.sprite.spritecollideany(self,snake.body):
            self.make_apple(snake)
    
    def draw(self,window):
        window.blit(self.image,self.rect)