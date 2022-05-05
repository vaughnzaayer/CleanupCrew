import pygame

from Button import Button
from MainMenu import MainMenu

class PauseMenuUI:

    def __init__(self, director):

        self.director = director

        self.elements = pygame.sprite.Group()

        self.resumeBtn = Button(560, 60, 'RESUME')
        self.resumeBtn.assignScene(self.director.scene)
        self.resumeBtn.assignDirector(self.director)
        self.resumeBtn.assignPosition(240 , (720 // 2) - 60)
        self.elements.add(self.resumeBtn)

        self.pausedText = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 60).render('PAUSED', True, (48, 255, 185))

        def resume():
            self.director.unpaused = True

        self.resumeBtn.assignFunction(resume)

        self.returnBtn = Button(560, 60, 'MAIN MENU')
        self.returnBtn.assignScene(self.director.scene)
        self.returnBtn.assignDirector(self.director)
        self.returnBtn.assignPosition(240 , (720 // 2) + 60)
        self.elements.add(self.returnBtn)

        def returnToMM():
            self.director.UIandStatsManager.playerHealth = 4
            self.director.UIandStatsManager.numberOfBullets = 10
            self.director.unpaused = True
            self.director.ingame = False
            self.director.renderUI = False
            self.director.UIandStatsManager.resetDataDrives()
            self.director.changeScene(MainMenu(self.director), None)

        self.returnBtn.assignFunction(returnToMM)

    def getElements(self):
        return self.elements
