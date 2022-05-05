import pygame

from SpriteSheet import SpriteSheet
from AnimationHandlerFW import AnimationHandler

class DataDrive(pygame.sprite.Sprite):

    def __init__(self, scene):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = SpriteSheet('Assets/DataDrive.png')
        self.animationManager = AnimationHandler(self.spriteSheet)
        self.animation = self.animationManager.createAnim([0, 1, 2, 3, 4, 5], 20, False)
        self.image = self.spriteSheet.parse_sprite('DataDrive 0.aseprite')
        self.rect = self.image.get_rect()

        self.frameCount = 10
        self.currentFrame = 0

        self.scene = scene
        self.player = self.scene.player

        self.scene.dataDrive = self


    def update(self):
        self.animation(self)
        if self.currentFrame % 5 == 0:
            if pygame.sprite.collide_rect(self, self.player):
                if self.scene.hasDataDrive != False:
                    self.scene.hasDataDrive = False
                    self.scene.MainMapManager.dir.UIandStatsManager.updateDrivesCollectedUI()
                self.kill()
                print('contact')
        self.currentFrame += 1
