import pygame

black = (0,0,0)

class Paddle(pugame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image,color,[0,0,width,height])

        self.rect = self.image.get_rect()

    def paddles_moving_up(self,no_of_pixels)
        self.rect.y -= no_of_pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def paddles_moving_down(self,no_of_pixels)
        self.rect.y += no_of_pixels
        if self.rect.y > 460:
            self.rect.y = 460