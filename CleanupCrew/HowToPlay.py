import pygame

from Scene import Scene
from Button import Button
from Player import Player

class HowToPlay(Scene):

    def __init__(self, director, mainMenu):
        Scene.__init__(self, director)

        self.allSprites = pygame.sprite.Group()
        self.player = Player()

        self.mainMenu = mainMenu

        self.backBtn = Button(480, 60, 'BACK')
        self.backBtn.assignScene(self)
        self.backBtn.assignPosition(100, 600)
        self.allSprites.add(self.backBtn)

        self.controlsSubtitle = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 60).render('CONTROLS', True, (48, 255, 185))

        self.ZToInteract = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 40).render('Z  TO  INTERACT', True, (11, 138, 143))
        self.XToMelee = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 40).render('X  TO  MELEE', True, (11, 138, 143))
        self.CToShoot = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 40).render('C  TO  SHOOT', True, (11, 138, 143))
        self.movement = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 40).render('ARROW  KEYS  TO  MOVE', True, (11, 138, 143))

        self.objective1 = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 60).render('COLLECT  ALL  3  DATA', True, (14, 175, 155))
        self.objective2 = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 60).render('DRIVES  TO  WIN', True, (14, 175, 155))

        def returnToMM():
            self.director.unpaused = True
            self.director.ingame = False
            self.director.renderUI = False
            self.director.changeScene(self.mainMenu, None)

        self.backBtn.assignFunction(returnToMM)

    def on_update(self):
        mousePosition = pygame.mouse.get_pos()
        self.backBtn.clickedOn(mousePosition)
        self.allSprites.update()

    def on_event(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.controlsSubtitle, (150, 100))
        screen.blit(self.ZToInteract, (150, 160))
        screen.blit(self.XToMelee, (150, 200))
        screen.blit(self.CToShoot, (150, 240))
        screen.blit(self.movement, (150, 280))

        screen.blit(self.objective1, (650, 270))
        screen.blit(self.objective2, (710, 330))


        self.allSprites.draw(screen)
