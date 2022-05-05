import pygame, sys

from Player import Player
from Scene import Scene
from Button import Button
from MainMenu import MainMenu


class MissionAccomplished(Scene):

    def __init__(self, director):
        Scene.__init__(self, director)

        self.allSprites = pygame.sprite.Group()
        self.player = Player()

        self.gameOverFont = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 80)
        self.gameOverText = self.gameOverFont.render('MISSION   ACCOMPLISHED', True, (48, 255, 185))

        self.quitBtn = Button(560, 60, 'QUIT')
        self.quitBtn.assignScene(self)
        self.quitBtn.assignPosition(340 , (720 // 2) + 120)
        self.allSprites.add(self.quitBtn)

        def quit():
            pygame.quit()
            sys.exit()

        self.quitBtn.assignFunction(quit)

        self.returnBtn = Button(560, 60, 'MAIN MENU')
        self.returnBtn.assignScene(self)
        self.returnBtn.assignPosition(340 , (720 // 2))
        self.allSprites.add(self.returnBtn)

        def returnToMM():
            self.director.UIandStatsManager.playerHealth = 4
            self.director.UIandStatsManager.numberOfBullets = 10
            self.director.unpaused = True
            self.director.ingame = False
            self.director.renderUI = False
            self.director.changeScene(MainMenu(self.director), None)

        self.returnBtn.assignFunction(returnToMM)

    def on_update(self):
        mousePosition = pygame.mouse.get_pos()
        self.director.UIandStatsManager.resetDataDrives()
        self.quitBtn.clickedOn(mousePosition)
        self.returnBtn.clickedOn(mousePosition)
        self.allSprites.update()


    def on_event(self):
        pass

    def on_draw(self, screen):
        self.allSprites.draw(screen)
        screen.blit(self.gameOverText, (1280 // 2 - 450, 720 // 2 - 150))
