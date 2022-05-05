import pygame

from SpriteSheet import SpriteSheet

class UIandStats:

    def __init__(self, director):
        self.sprite_sheet = SpriteSheet('Assets/UISpriteSheet.png')
        self.driveSprite_sheet = SpriteSheet('Assets/DataDrive.png')
        self.director = director

        self.playerHealth = 4
        self.numberOfBullets = 10
        self.drivesCollected = 0

        self.allElements = pygame.sprite.Group()

        self.healthBatteryIMGS = [self.sprite_sheet.parse_sprite('UISpriteSheet 0.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 1.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 2.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 3.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 4.aseprite')]
        # for image in self.healthBatteryIMGS:
        #     self.healthBatteryIMGS[self.healthBatteryIMGS.index(image)] = pygame.transform.scale(image, (120, 120))


        self.healthBattery = pygame.sprite.Sprite()
        self.healthBattery.image = self.healthBatteryIMGS[0]
        self.healthBattery.rect = self.healthBattery.image.get_rect()
        self.healthBattery.rect.x = 1060
        self.healthBattery.rect.y = 20
        self.allElements.add(self.healthBattery)


        self.portrait = pygame.sprite.Sprite()
        self.portrait.image = self.sprite_sheet.parse_sprite('UISpriteSheet 5.aseprite')
        # self.portrait.image = pygame.transform.scale(self.portrait.image, (120, 120))
        self.portrait.rect = self.portrait.image.get_rect()
        self.portrait.rect.x = 1140
        self.portrait.rect.y = 20
        self.allElements.add(self.portrait)

        self.driveElements = []
        offset = 0
        for drive in range(3):
            newDrive = pygame.sprite.Sprite()
            newDrive.image = self.driveSprite_sheet.parse_sprite('DataDrive 0.aseprite')
            newDrive.rect = newDrive.image.get_rect()
            newDrive.rect.x = 1120 + offset
            newDrive.rect.y = 140
            self.driveElements.append(newDrive)
            offset += 40




        self.handgun = pygame.sprite.Sprite()
        self.handgun.image = self.sprite_sheet.parse_sprite('UISpriteSheet 6.aseprite')
        # self.handgun.image = pygame.transform.scale(self.handgun.image, (120, 120))
        self.handgun.rect = self.handgun.image.get_rect()
        self.handgun.rect.x = 35
        self.handgun.rect.y = 20
        self.allElements.add(self.handgun)

        self.bullet = pygame.sprite.Sprite()
        self.bullet.image = self.sprite_sheet.parse_sprite('UISpriteSheet 7.aseprite')
        # self.bullet.image = pygame.transform.scale(self.bullet.image, (120, 120))
        self.bullet.rect = self.bullet.image.get_rect()
        self.bullet.rect.x = 10
        self.bullet.rect.y = 120
        self.allElements.add(self.bullet)

        self.ammoCount = pygame.sprite.Sprite()
        self.ammoCount.image = pygame.Surface([120, 120])
        # self.ammoCount.image = self.ammoCount.image.convert_alpha()
        self.ammoCount.rect = self.ammoCount.image.get_rect()
        self.ammoCount.rect.x = 100
        self.ammoCount.rect.y = 160
        self.ammoCountFont = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 50)
        # self.allElements.add(self.ammoCount)

        self.escapeMessage = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 30).render('MISSION  ACCOMPLISHED    RETURN  TO  AIRLOCK', True, (48, 255, 185))

    def resetDataDrives(self):
        self.drivesCollected = 0
        for drive in self.driveElements:
            drive.kill()

    def getUIRender(self):
        return self.allElements

    def updateDrivesCollectedUI(self):
        self.drivesCollected += 1
        self.director.UIRender.add(self.driveElements[self.drivesCollected - 1])
        self.director.UIRender.update()

    def updateUIRender(self, screen):
        self.ammoCountNumber = self.ammoCountFont.render('x' + str(self.numberOfBullets), True, (48, 255, 185))
        screen.blit(self.ammoCountNumber, (self.ammoCount.rect.x, self.ammoCount.rect.y))
        self.healthBattery.image = self.healthBatteryIMGS[4 - self.playerHealth]
        if self.drivesCollected == 3:
            screen.blit(self.escapeMessage, (1280 // 2 - 310, 30))
