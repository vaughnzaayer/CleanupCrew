import pygame, random
from Scene import Scene
from Walls import Wall
from Player import Player
from Enemy import Enemy
from Door import Door
from Hatch import Hatch
from Ladder import Ladder
from DataDrive import DataDrive
from Physics import *



# A room is a type of scene, but should report to the MMM instead of the scene director


class Room(Scene):

    def __init__(self, color, willSpawnEnemies):
        self.MainMapManager = None

        self.frameCount = 0

        self.color = color

        self.willSpawnEnemies = willSpawnEnemies

        self.right = None
        self.left = None
        self.down = None
        self.up = None

        self.player = Player()
        self.player.rect.x = 1280 // 2
        self.player.rect.y = 580
        self.player.scene = self



        self.LEFT_DOOR_COORDS = [20, 560]
        self.RIGHT_DOOR_COORDS = [1180 ,560]
        self.TOP_HATCH_COORDS = [1280 // 2, 20]
        self.BOTTOM_HATCH_COORDS = [1280 // 2, 680]

        self.doors = pygame.sprite.Group()

        if self.left != None:
            self.doorL = Door()
            self.doorL.rect.x = self.LEFT_DOOR_COORDS[0]
            self.doorL.rect.y = self.LEFT_DOOR_COORDS[1]
            self.doorL.room = self
            self.doors.add(self.doorL)

        if self.right != None:
            self.doorR = Door()
            self.doorR.rect.x = self.RIGHT_DOOR_COORDS[0]
            self.doorR.rect.y = self.RIGHT_DOOR_COORDS[1]
            self.doorR.room = self
            self.doors.add(self.doorR)

        if self.up != None:
            self.doorU = Hatch()
            self.doorU.rect.x = self.TOP_HATCH_COORDS[0]
            self.doorU.rect.y = self.TOP_HATCH_COORDS[1]
            self.doorU.room = self
            self.doors.add(self.doorU)

        if self.down != None:
            self.doorD = Hatch()
            self.doorD.rect.x = self.BOTTOM_HATCH_COORDS[0]
            self.doorD.rect.y = self.BOTTOM_HATCH_COORDS[1]
            self.doorD.room = self
            self.doors.add(self.doorD)


        self.wallNorth = Wall('Horizontal', self.color)
        self.wallSouth = Wall('Horizontal', self.color)
        self.wallEast = Wall('Vertical', self.color)
        self.wallWest = Wall('Vertical', self.color)

        self.activeSprites = pygame.sprite.Group()
        self.vertWallsList = pygame.sprite.Group()
        self.horizWallsList = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()

        self.dataDrive = None
        self.dataDriveGroup = pygame.sprite.Group()
        self.hasDataDrive = False


        self.listOfWalls = [self.wallNorth, self.wallSouth, self.wallEast, self.wallWest]

        self.moveWalls()

        self.vertWallsList.add(self.wallEast)
        self.vertWallsList.add(self.wallWest)

        self.horizWallsList.add(self.wallSouth)
        self.horizWallsList.add(self.wallNorth)

        self.floors.add(self.wallSouth)

        self.activeSprites.add(self.doors)
        self.activeSprites.add(self.ladders)
        self.activeSprites.add(self.player)
        self.activeSprites.add(self.projectiles)
        self.activeSprites.add(self.vertWallsList)
        self.activeSprites.add(self.horizWallsList)
        self.activeSprites.add(self.floors)

        self.enemySprites = pygame.sprite.Group()

        if self.willSpawnEnemies:

            numberOfEnemies = random.randint(0, 100)
            if numberOfEnemies < 10:
                numberOfEnemies = 0
            elif numberOfEnemies < 50:
                numberOfEnemies = 1
            elif numberOfEnemies < 90:
                numberOfEnemies = 2
            elif numberOfEnemies < 100:
                numberOfEnemies = 3

            i = 0
            while i < numberOfEnemies:


                enemy = Enemy()
                enemy.rect.x = random.randint(20, 1140)
                enemy.rect.y = 575

                self.activeSprites.add(enemy)
                self.enemySprites.add(enemy)
                enemy.vertWalls = self.vertWallsList
                enemy.horizWalls = self.horizWallsList
                enemy.floors = self.floors
                enemy.trackingPlayer = self.player
                enemy.scene = self

                self.player.enemies = self.enemySprites

                i += 1

            # self.enemy = Enemy()
            # self.enemy.rect.x = random.randint(20, 1260)
            # self.enemy.rect.y = 575
            #
            # self.activeSprites.add(self.enemy)
            # self.enemySprites.add(self.enemy)
            # self.enemy.vertWalls = self.vertWallsList
            # self.enemy.horizWalls = self.horizWallsList
            # self.enemy.floors = self.floors
            # self.enemy.trackingPlayer = self.player
            # self.enemy.scene = self
            #
            # self.player.enemies = self.enemySprites

        self.player.vertWalls = self.vertWallsList
        self.player.horizWalls = self.horizWallsList
        self.player.floors = self.floors
        self.player.doors = self.doors
        self.player.ladders = self.ladders





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
            self.doorR.room = self
            self.doorR.assignDirection('right')
            self.doorR.assignTransScene(room)
            self.doors.add(self.doorR)


    def assignLeft(self, room):
        self.left = room
        if self.left != None:
            self.doorL = Door()
            self.doorL.rect.x = self.LEFT_DOOR_COORDS[0]
            self.doorL.rect.y = self.LEFT_DOOR_COORDS[1]
            self.doorL.room = self
            self.doorL.assignDirection('left')
            self.doorL.assignTransScene(room)
            self.doors.add(self.doorL)

    def assignUp(self, room):
        self.up = room
        if self.up != None:
            self.doorU = Hatch()
            self.doorU.rect.x = self.TOP_HATCH_COORDS[0]
            self.doorU.rect.y = self.TOP_HATCH_COORDS[1]
            self.doorU.room = self
            self.doorU.assignDirection('up')
            self.doorU.assignTransScene(room)
            self.doors.add(self.doorU)

    def assignDown(self, room):
        self.down = room
        if self.down != None:
            self.doorD = Hatch()
            self.doorD.rect.x = self.BOTTOM_HATCH_COORDS[0]
            self.doorD.rect.y = self.BOTTOM_HATCH_COORDS[1]
            self.doorD.room = self
            self.doorD.assignDirection('down')
            self.doorD.assignTransScene(room)
            self.doors.add(self.doorD)


    def updateRender(self):
        self.doors.update()
        self.activeSprites.update()

        for door in self.doors:
            if door.rect.y == 560: # If the door is a left/right
                if door.rect.x == 20: # If door is left
                    # door.assignOpposite(self.RIGHT_DOOR_COORDS)
                    door.assignOpposite([1140, 580])
                    print('LEFT DOOR Updated')
                    print(door.opposite)
                else: # If door is right
                    door.assignOpposite([20, 580])
                    print('RIGHT DOOR Updated')
                    print(door.opposite)
            else: # If the door is an up/down

                if door.rect.y == 20: # If door is up
                    # door.assignOpposite(self.TOP_HATCH_COORDS)
                    door.assignOpposite([640, 580])
                    print('TOP DOOR Updated')
                    print(door.opposite)
                else: # If door is down
                    # door.assignOpposite(self.BOTTOM_HATCH_COORDS)
                    door.assignOpposite([640, 20])
                    print('BOTTOM DOOR Updated')
                    print(door.opposite)


        if self.up != None:
            numberOfLadders = 6
            i = 0
            while i < numberOfLadders:
                newLadder = Ladder(self)
                self.ladders.add(newLadder)
                self.player.ladders.add(newLadder)
                newLadder.rect.x = 615
                newLadder.rect.y = 120 * i
                i += 1

        if self.hasDataDrive:
            self.dataDrive = DataDrive(self)
            self.dataDrive.rect.x = 1280 // 2
            self.dataDrive.rect.y = 720 // 2
            self.dataDriveGroup.add(self.dataDrive)




    def resetPlayerPos(self, playerPos):
        self.player.velocity = Vector2D(0.0, 0.0)
        self.player.rect.x = playerPos[0]
        self.player.rect.y = playerPos[1]

    def on_event(self):
        pass

    def on_update(self):
        self.dataDriveGroup.update()
        self.doors.update()
        self.activeSprites.update()
        self.player.update()


    def on_draw(self, screen):
        self.ladders.draw(screen)
        self.doors.draw(screen)
        self.dataDriveGroup.draw(screen)
        self.activeSprites.draw(screen)











        # self.wallVert = pygame.Surface([20, 720])
        # self.wallVert.fill((255, 0, 0))
        # self.wallVertRect = self.wallVert.get_rect()
        #
        # self.wallHoriz = pygame.Surface([1280, 20])
        # self.wallHoriz.fill((255, 0, 0))
        # self.wallHorizRect = self.wallHoriz.get_rect()
        #
        # self.playerEnterCoords = playerEnterCoords
