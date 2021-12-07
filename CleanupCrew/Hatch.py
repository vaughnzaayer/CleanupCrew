import pygame
from Door import Door

class Hatch(Door):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80, 20])
        self.image.fill((14, 175, 155))
        self.rect = self.image.get_rect()
