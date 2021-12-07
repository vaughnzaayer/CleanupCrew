from Scene import Scene
from Button import Button
from Player import Player

import pygame, sys


class MainMenu(Scene):


    def __init__(self, director):
        Scene.__init__(self, director)

        self.allSprites = pygame.sprite.Group()
        self.player = Player()

        self.quitBtn = Button(560, 60, 'QUIT')
        self.quitBtn.assignScene(self)
        self.quitBtn.assignPosition(120 , (720 // 2) - 60)
        self.allSprites.add(self.quitBtn)

        def quit():
            pygame.quit()
            sys.exit()

        self.quitBtn.assignFunction(quit)

        self.startBtn = Button(560, 60, 'INITIATE')
        self.startBtn.assignScene(self)
        self.startBtn.assignPosition(120 , (720 // 2) - 160)
        self.allSprites.add(self.startBtn)

        def start():
            self.director.startMMM()

        self.startBtn.assignFunction(start)





    def on_update(self):
        self.quitBtn.clickedOn(pygame.mouse.get_pos())
        self.startBtn.clickedOn(pygame.mouse.get_pos())
        self.allSprites.update()

    def on_event(self):
        pass

    def on_draw(self, screen):
        self.allSprites.draw(screen)
        screen.blit(self.director.version, (0, 700))
