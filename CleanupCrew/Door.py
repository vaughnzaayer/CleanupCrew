import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80, 140])
        self.image.fill((14, 175, 155))
        self.rect = self.image.get_rect()
        self.toScene = None
        self.fromDirection = None
        self.room = None
        self.opposite = None


    def transScene(self):
        self.room.MainMapManager.dir.changeScene(self.toScene, self.opposite)

    def assignTransScene(self, scene):
        self.toScene = scene

    def assignDirection(self, direction):
        self.fromDirection = direction

    def assignOpposite(self, opposite):
        self.opposite = opposite
