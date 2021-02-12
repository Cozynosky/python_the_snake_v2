"""
file with snake class
"""
import settings
import pygame


class Snake:
    def __init__(self):
        self.make_snake()

    # metod making new snake
    def make_snake(self):
        self.head = BodyPart(192, 224)
        self.facing = "left"
        self.body = pygame.sprite.Group()
        self.body.add(BodyPart(208, 224))
        self.body.add(BodyPart(224, 224))
        # flag to know snake just ate apple
        self.grow = False

    # updating head and body positions
    def update(self):
        self.move_body()
        self.move_head()

    # move head
    def move_head(self):
        if self.facing == "left":
            self.head.rect.x -= 16
        elif self.facing == "right":
            self.head.rect.x += 16
        elif self.facing == "up":
            self.head.rect.y -= 16
        elif self.facing == "down":
            self.head.rect.y += 16

    # move body parts
    def move_body(self):
        new_pos = self.head.rect
        temp_body = pygame.sprite.Group()
        for part in self.body:
            temp_body.add(BodyPart(new_pos.x, new_pos.y))
            new_pos = part.rect
        self.body = temp_body
        # if snake ate apple make it bigger
        if self.grow:
            self.body.add(BodyPart(new_pos.x, new_pos.y))
            self.grow = False

    # detect wall collision
    def wall_collision(self):
        if self.head.rect.top < 80:
            return True
        elif self.head.rect.bottom > 448:
            return True
        elif self.head.rect.left < 32:
            return True
        elif self.head.rect.right > 384:
            return True
        return False

    # detect self collision
    def self_collision(self):
        if pygame.sprite.spritecollideany(self.head, self.body):
            return True
        return False

    # apple collision method
    def apple_collision(self, apple):
        if self.head.rect.colliderect(apple.rect):
            return True
        return False

    # draw parts on the screen
    def draw(self, window):
        self.head.draw(window)
        self.body.draw(window)


class BodyPart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 16, 16)
        self.image = pygame.Surface((16, 16))
        self.image.fill(settings.SNAKE_COLOR)

    def draw(self, window):
        window.blit(self.image, self.rect)
