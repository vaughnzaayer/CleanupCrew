import pygame
from Scene import Scene
from Walls import Wall
from Player import Player
from Door import Door
from Hatch import Hatch


class Room(Scene):

    def __init__(self):

        self.MainMapManager = None

        self.color = (115, 115, 115)


        self.right = None
        self.left = None
        self.down = None
        self.up = None

        self.wallNorth = None
        self.wallSouth = None
        self.wallEast = None
        self.wallWest = None

        self.doorR = None
        self.doorL = None
        self.doorU = None
        self.doorD = None

        self.LEFT_DOOR_COORDS = [20, 560]
        self.RIGHT_DOOR_COORDS = [1180 ,560]
        self.TOP_HATCH_COORDS = [1280 // 2, 20]
        self.BOTTOM_HATCH_COORDS = [1280 // 2, 680]

        self.doors = pygame.sprite.Group()
        self.activeSprites = pygame.sprite.Group()
        self.vertWallsList = pygame.sprite.Group()
        self.horizWallsList = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()

        self.player = None

        self.assignPlayer()


    def createWalls(self):
        self.wallNorth = Wall('Horizontal', self.color)
        self.wallSouth = Wall('Horizontal', self.color)
        self.wallEast = Wall('Vertical', self.color)
        self.wallWest = Wall('Vertical', self.color)

        self.moveWalls()

        self.vertWallsList.add(self.wallEast)
        self.vertWallsList.add(self.wallWest)

        self.horizWallsList.add(self.wallSouth)
        self.horizWallsList.add(self.wallNorth)

        self.floors.add(self.wallSouth)

    def moveWalls(self):
        self.wallNorth.rect.x = 0
        self.wallNorth.rect.y = 0

        self.wallSouth.rect.x = 0
        self.wallSouth.rect.y = 700

        self.wallEast.rect.x = 1260
        self.wallEast.rect.y = 0

        self.wallWest.rect.x = 0
        self.wallWest.rect.y = 0

    def assignRight(self, room):
        self.right = room
        if self.right != None:
            self.doorR = Door()
            self.doorR.rect.x = self.RIGHT_DOOR_COORDS[0]
            self.doorR.rect.y = self.RIGHT_DOOR_COORDS[1]
            self.doorR.assignDirection('right')
            self.doorR.assignTransScene(room)
            self.doors.add(self.doorR)


    def assignLeft(self, room):
        self.left = room
        if self.left != None:
            self.doorL = Door()
            self.doorL.rect.x = self.LEFT_DOOR_COORDS[0]
            self.doorL.rect.y = self.LEFT_DOOR_COORDS[1]
            self.doorL.assignDirection('left')
            self.doorL.assignTransScene(room)
            self.doors.add(self.doorL)

    def assignUp(self, room):
        self.up = room
        if self.up != None:
            self.doorU = Hatch()
            self.doorU.rect.x = self.TOP_HATCH_COORDS[0]
            self.doorU.rect.y = self.TOP_HATCH_COORDS[1]
            self.doorU.assignDirection('up')
            self.doorU.assignTransScene(room)
            self.doors.add(self.doorU)

    def assignDown(self, room):
        self.down = room
        if self.down != None:
            self.doorD = Hatch()
            self.doorD.rect.x = self.BOTTOM_HATCH_COORDS[0]
            self.doorD.rect.y = self.BOTTOM_HATCH_COORDS[1]
            self.doorD.assignDirection('down')
            self.doorD.assignTransScene(room)
            self.doors.add(self.doorD)

    def assignPlayer(self):
        self.player = Player()
        self.player.vertWalls = self.vertWallsList
        self.player.horizWalls = self.horizWallsList
        self.player.floors = self.floors
        self.player.doors = self.doors

    def assembleRoom(self):
        self.createWalls()
        self.activeSprites.update()

    def on_event(self):
        pass

    def on_update(self):
        self.player.update()
        self.activeSprites.update()

    def on_draw(self, screen):
        self.activeSprites.draw(screen)
