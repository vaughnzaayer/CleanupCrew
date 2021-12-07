import pygame
from SpriteSheet import SpriteSheet

class Ladder(pygame.sprite.Sprite):

    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = SpriteSheet('Assets/Ladder.png')
        self.image = self.spriteSheet.parse_sprite('Ladder.aseprite')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()

        self.scene = scene

        self.scene.ladders.add(self)
