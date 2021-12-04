import pygame
from random import randint

black = (0,0,0)

class Ball(pugame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image,color,[0,0,width,height])

        self.velocity = [randint(4,8),randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bouncing(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = self.velocity[1]