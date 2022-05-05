from Scene import Scene
from Button import Button
from Player import Player
from HowToPlay import HowToPlay

import pygame, sys


class MainMenu(Scene):


    def __init__(self, director):
        Scene.__init__(self, director)

        self.allSprites = pygame.sprite.Group()
        self.buttons = []
        self.player = Player()

        self.quitBtn = Button(480, 60, 'QUIT')
        self.quitBtn.assignScene(self)
        self.quitBtn.assignPosition(100 , (720 // 2) - 60)
        self.allSprites.add(self.quitBtn)
        self.buttons.append(self.quitBtn)

        def quit():
            pygame.quit()
            sys.exit()

        self.quitBtn.assignFunction(quit)

        self.startBtn = Button(480, 60, 'INITIATE')
        self.startBtn.assignScene(self)
        self.startBtn.assignPosition(100 , (720 // 2) - 160)
        self.allSprites.add(self.startBtn)
        self.buttons.append(self.startBtn)

        def start():
            self.director.startMMM()

        self.startBtn.assignFunction(start)
        self.htpBtn = Button(480, 60, 'HOW  TO  PLAY')
        self.htpBtn.assignScene(self)
        self.htpBtn.assignPosition(600, 600)
        self.allSprites.add(self.htpBtn)

        def howToPlay():
            self.director.changeScene(HowToPlay(self.director, self), None)

        self.htpBtn.assignFunction(howToPlay)

        self.mainTitle1 = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 120).render('CLEANUP', True, (14, 175, 155))
        self.mainTitle2 = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 160).render('CREW', True, (48, 255, 185))




    def on_update(self):
        mousePosition = pygame.mouse.get_pos()
        self.quitBtn.clickedOn(mousePosition)
        self.startBtn.clickedOn(mousePosition)
        self.htpBtn.clickedOn(mousePosition)
        self.allSprites.update()

    def on_event(self):
        pass

    def on_draw(self, screen):
        self.allSprites.draw(screen)
        screen.blit(self.mainTitle1, (1280 // 2 + 40, 150))
        screen.blit(self.mainTitle2, (1280 // 2 + 90, 220))
        screen.blit(self.director.version, (0, 700))
        screen.blit(self.director.author, (1150, 700))
