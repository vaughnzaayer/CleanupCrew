import pygame
from Physics import *


class Projectile(pygame.sprite.Sprite):

    def __init__(self, color, heading, scene):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.heading = heading
        self.scene = scene

        self.image = pygame.Surface([12, 8])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.scene.activeSprites.add(self)
        self.scene.projectiles.add(self)

        self.velocity = Vector2D(0, 0)
        if self.heading > 0:
            self.velocity.dx = 10
        else:
            self.velocity.dx = -10

    def update(self):
        self.rect.x += self.velocity.dx

        for wall in self.scene.vertWallsList.sprites():
            if pygame.sprite.collide_rect(self, wall) == True:
                self.kill()
