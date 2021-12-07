import pygame

from SpriteSheet import SpriteSheet

class UIandStats:

    def __init__(self, director):
        self.sprite_sheet = SpriteSheet('Assets/UISpriteSheet.png')
        self.director = director

        self.playerHealth = 4
        self.numberOfBullets = 10

        self.allElements = pygame.sprite.Group()

        self.healthBatteryIMGS = [self.sprite_sheet.parse_sprite('UISpriteSheet 0.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 1.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 2.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 3.aseprite'), self.sprite_sheet.parse_sprite('UISpriteSheet 4.aseprite')]
        for image in self.healthBatteryIMGS:
            self.healthBatteryIMGS[self.healthBatteryIMGS.index(image)] = pygame.transform.scale(image, (120, 120))


        self.healthBattery = pygame.sprite.Sprite()
        self.healthBattery.image = self.healthBatteryIMGS[0]
        self.healthBattery.rect = self.healthBattery.image.get_rect()
        self.healthBattery.rect.x = 1060
        self.healthBattery.rect.y = 20
        self.allElements.add(self.healthBattery)


        self.portrait = pygame.sprite.Sprite()
        self.portrait.image = self.sprite_sheet.parse_sprite('UISpriteSheet 5.aseprite')
        self.portrait.image = pygame.transform.scale(self.portrait.image, (120, 120))
        self.portrait.rect = self.portrait.image.get_rect()
        self.portrait.rect.x = 1140
        self.portrait.rect.y = 20
        self.allElements.add(self.portrait)

        self.handgun = pygame.sprite.Sprite()
        self.handgun.image = self.sprite_sheet.parse_sprite('UISpriteSheet 6.aseprite')
        self.handgun.image = pygame.transform.scale(self.handgun.image, (120, 120))
        self.handgun.rect = self.handgun.image.get_rect()
        self.handgun.rect.x = 35
        self.handgun.rect.y = 20
        self.allElements.add(self.handgun)

        self.bullet = pygame.sprite.Sprite()
        self.bullet.image = self.sprite_sheet.parse_sprite('UISpriteSheet 7.aseprite')
        self.bullet.image = pygame.transform.scale(self.bullet.image, (120, 120))
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

    def getUIRender(self):
        return self.allElements

    def updateUIRender(self, screen):
        self.ammoCountNumber = self.ammoCountFont.render('x' + str(self.numberOfBullets), True, (48, 255, 185))
        screen.blit(self.ammoCountNumber, (self.ammoCount.rect.x, self.ammoCount.rect.y))
        self.healthBattery.image = self.healthBatteryIMGS[4 - self.playerHealth]
