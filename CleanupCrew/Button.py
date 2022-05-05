import pygame
from Physics import *

class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, label):
        pygame.sprite.Sprite.__init__(self)
        if pygame.get_init() == False:
            pygame.init()
            pygame.font.init()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill((11, 138, 143))
        self.rect = self.image.get_rect()
        self.labelTxt = label
        self.func = None
        self.scene = None
        self.director = None
        self.font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', height)
        self.btnTxt = self.font.render(self.labelTxt, True, (99, 27, 52))
        self.image.blit(self.btnTxt, (self.rect.x + 40, self.rect.y))

        # Impose text here

    def assignDirector(self, director):
        self.director = director

    def assignScene(self, scene):
        self.scene = scene

    def assignPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def onClick(self):
        self.func()

    def assignFunction(self, function):
        self.func = function

    def mouseOver(self, mousePos):
        if self.rect.x <= mousePos[0] <= self.rect.x + self.width and self.rect.y <= mousePos[1] <= self.rect.y + self.height:
            # self.image.fill((99, 27, 52))
            return True
        else:
            # self.image.fill((11, 138, 143))
            return False

    def clickedOn(self, mousePos):
        if self.scene.director.click:
            print('boop')
            if self.mouseOver(mousePos):
                self.onClick()

    def clickedOnDirector(self, mousePos):
        if self.director.click:
            print('boop')
            if self.mouseOver(mousePos):
                self.onClick()

    def updateButton(self, mousePos):
        if self.mouseOver(mousePos):
            self.image.fill((99, 27, 52))
            self.btnTxt = self.font.render(self.labelTxt, True, (11, 138, 143))
            self.image.blit(self.btnTxt, (self.rect.x + 40, self.rect.y))
        else:
            self.image.fill((11, 138, 143))
            self.btnTxt = self.font.render(self.labelTxt, True, (99, 27, 52))
            self.image.blit(self.btnTxt, (self.rect.x + 40, self.rect.y))
