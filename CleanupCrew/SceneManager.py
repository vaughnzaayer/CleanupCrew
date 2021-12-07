import pygame, sys
from Player import Player
from MainMapManager import MainMapManager
from UIandStatsManager import UIandStats

class Director:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Cleanup Crew')
        gameIcon = pygame.image.load('Assets/ICON.png')
        pygame.display.set_icon(gameIcon)
        self.scene = None
        self.quit_signal = False
        self.clock = pygame.time.Clock()
        self.MainMapManager = MainMapManager(14)
        self.MainMapManager.dir = self
        self.UIandStatsManager = UIandStats(self)
        self.UIRender = self.UIandStatsManager.getUIRender()
        self.renderUI = False
        self.click = False
        self.unpaused = True
        self.verFont = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 20)
        self.version = self.verFont.render('ALPHA   0 0 5', True, (48, 255, 185))
        self.screen.blit(self.version, (0, 700))



    def loop(self):
        # --- MAIN GAME LOOP ---

        while self.quit_signal == False:
            time = self.clock.tick(60)

            # -- EXIT EVENTS --
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
                else:
                    self.click = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.scene.player.vertMove(-1)
                    if event.key == pygame.K_RIGHT:
                        self.scene.player.vertMove(1)

                    if event.key == pygame.K_z:
                        self.scene.player.interact()

                    if event.key == pygame.K_x:
                        self.scene.player.meleeAttack()

                    if event.key == pygame.K_c:
                        self.scene.player.rangedAttack()

                    if event.key == pygame.K_UP:
                        if self.scene.player.isTouchingLadder == False:
                            self.scene.player.jump()
                        else:
                            self.scene.player.velocity.dy = -2

                    if event.key == pygame.K_DOWN:
                        if self.scene.player.isTouchingLadder == True:
                            self.scene.player.velocity.dy = 2

                    if event.key == pygame.K_ESCAPE:
                        if self.unpaused:
                            self.unpaused = False
                        else:
                            self.unpaused = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.scene.player.vertMove(0)

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        if self.scene.player.isTouchingLadder == True:
                            self.scene.player.velocity.dy = 0

            if self.unpaused:
                # -- EVENT DETECTION --
                self.scene.on_event()

                # -- SCREEN UPDATE --
                self.scene.on_update()
                pygame.display.update()

                # -- DRAW THE SCREEN --
                self.screen.fill((65, 29, 49))
                self.scene.on_draw(self.screen)
                self.scene.player.hitBoxes.draw(self.screen)
                if self.renderUI:
                    self.UIRender.draw(self.screen)
                    self.UIandStatsManager.updateUIRender(self.screen)
                pygame.display.flip()

    def changeScene(self, scene, playerPos):
        self.scene = scene
        if playerPos != None:
            self.scene.resetPlayerPos(playerPos)



    def startMMM(self):
        self.scene = self.MainMapManager.beginPlayer()
        self.renderUI = True

    def quit(self):
        self.quit_signal = True
