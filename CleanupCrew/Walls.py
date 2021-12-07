import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, type, color):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if type == 'Vertical':
            self.image = pygame.Surface([20, 720])
            self.image.fill(color)
            self.rect = self.image.get_rect()
        elif type == 'Horizontal':
            self.image = pygame.Surface([1280, 20])
            self.image.fill(color)
            self.rect = self.image.get_rect()
