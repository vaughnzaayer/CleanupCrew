from Player import Player
from Scene import Scene
import pygame

class TestScene(Scene):

    def __init__(self, director):
        print('Verify')
        self.director = director
        self.player = Player()
        self.player.rect.x = 0
        self.player.rect.y = 0
        self.activeSprites = pygame.sprite.Group()
        self.activeSprites.add(self.player)



    def on_event(self):
        pass

    def on_update(self):
        self.player.update()
        self.activeSprites.update()

    def on_draw(self, screen):
        self.activeSprites.draw(screen)
