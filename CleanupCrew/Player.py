import pygame
from SpriteSheet import SpriteSheet
from AnimationHandlerFW import AnimationHandler
from Physics import *
from Projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = SpriteSheet('Assets/MCAnimUPSCALE.png')

        self.animationManager = AnimationHandler(self.sprite_sheet)

        self.image = self.sprite_sheet.parse_sprite('MCAnimUPSCALE 0.aseprite')
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, 0)

        self.forwardHB = pygame.sprite.Sprite()
        self.forwardHB.image = pygame.Surface([10, 120], pygame.SRCALPHA)
        self.forwardHB.image = self.forwardHB.image.convert_alpha()
        self.forwardHB.rect = self.forwardHB.image.get_rect()
        self.forwardHB.rect.x = self.rect.x + 90
        self.forwardHB.rect.y = self.rect.y

        self.backwardHB = pygame.sprite.Sprite()
        self.backwardHB.image = pygame.Surface([10, 120], pygame.SRCALPHA)
        self.backwardHB.image = self.backwardHB.image.convert_alpha()
        self.backwardHB.rect = self.backwardHB.image.get_rect()
        self.backwardHB.rect.x = self.rect.x - 10
        self.backwardHB.rect.y = self.rect.y

        self.hitBoxes = pygame.sprite.Group()
        self.hitBoxes.add(self.backwardHB)
        self.hitBoxes.add(self.forwardHB)

        self.gravity = 0.25
        self.velocity = Vector2D(0.0, 0.0)

        self.vertWalls = None
        self.horizWalls = None
        self.floors = None
        self.doors = None
        self.enemies = None
        self.ladders = None

        self.scene = None

        self.isOnGround = False
        self.isTouchingDoor = False
        self.doorContact = None
        self.isTouchingLadder = False

        self.isAttackingMelee = False
        self.isAttackingRanged = False
        self.facingRight = True
        self.frameCount = 0
        self.currentFrame = 0

        self.coolDownFramesMelee = 60
        self.coolDownFramesRanged = 40
        self.currCoolDownNum = 0

        self.iFrames = 0

        self.idleAnim, self.idleAnimRev = self.animationManager.createAnim([0, 1], 60, True)
        self.runAnim, self.runAnimRev = self.animationManager.createAnim([2, 3, 4, 5, 6, 7], 15, True)
        self.meleeAttackAnim, self.meleeAttackAnimRev = self.animationManager.createAnim([8, 9, 10, 11, 12, 13], 10, True)
        self.rangeAttackAnim, self.rangeAttackAnimRev = self.animationManager.createAnim([14, 15, 16, 17], 10, True)
        self.ladderClimbingAnim = self.animationManager.createAnim([18, 19, 20, 21], 20, False)

    def vertMove(self, x):
        if x == -1:
            self.velocity.dx = -3.0
            self.facingRight = False
        if x == 1:
            self.velocity.dx = 3.0
            self.facingRight = True
        if x == 0:
            self.velocity.dx = 0

    def jump(self):
        if self.isOnGround:
            self.velocity.dy = -10

    def gravUpdate(self):
        if not self.isOnGround:
            self.velocity.dy += self.gravity

    def interact(self):
        if self.isTouchingDoor:
            print('Interacted!')
            print(self.doorContact.toScene)
            self.doorContact.transScene()
        else:
            print('ERROR! No object detected')
            print(str(self.doorContact))

    def meleeAttack(self):
        self.isAttackingMelee = True
        self.currCoolDownNum += 1

    def rangedAttack(self):
        if self.currCoolDownNum == 0:
            numberOfBullets = self.scene.MainMapManager.dir.UIandStatsManager.numberOfBullets
            if numberOfBullets > 0:
                self.scene.MainMapManager.dir.UIandStatsManager.numberOfBullets -= 1
                if self.facingRight:
                    newProjectile = Projectile((50, 83, 95), 1, self.scene)
                    newProjectile.rect.x = self.rect.x + 90
                    newProjectile.rect.y = self.rect.y + 40
                else:
                    newProjectile = Projectile((50, 83, 95), -1, self.scene)
                    newProjectile.rect.x = self.rect.x
                    newProjectile.rect.y = self.rect.y + 40

            print('spawned')


        self.isAttackingRanged = True
        self.currCoolDownNum += 1




    def update(self):
        # print(str(self.rect.x) + ' ' + str(self.rect.y))

        # Box updates

        self.forwardHB.rect.x = self.rect.x + 120
        self.forwardHB.rect.y = self.rect.y

        self.backwardHB.rect.x = self.rect.x - 30
        self.backwardHB.rect.y = self.rect.y

        # Animation updates

        if self.isAttackingMelee == False and self.isAttackingRanged == False:
            if self.velocity.dx == 0:
                if self.facingRight:
                    self.idleAnim(self)
                else:
                    self.idleAnimRev(self)

            elif self.velocity.dx > 0:
                self.runAnim(self)
            else:
                self.runAnimRev(self)
        elif self.isAttackingMelee == True and self.currCoolDownNum > 0:
            self.velocity.dx = 0
            if self.facingRight:
                self.meleeAttackAnim(self)
            else:
                self.meleeAttackAnimRev(self)

        elif self.isAttackingRanged == True and self.currCoolDownNum > 0 and self.scene.MainMapManager.dir.UIandStatsManager.numberOfBullets > 0:
            self.velocity.dx = 0
            if self.facingRight:
                self.rangeAttackAnim(self)
            else:
                self.rangeAttackAnimRev(self)

        if self.currCoolDownNum != 0:
            self.currCoolDownNum += 1
            if self.currCoolDownNum >= self.coolDownFramesMelee:
                self.currCoolDownNum = 0
                self.isAttackingMelee = False
            if self.currCoolDownNum >= self.coolDownFramesRanged:
                self.isAttackingRanged = False



        # Updating position based on movement
        self.rect.x += self.velocity.dx

        # Updating position based on gravity
        if not self.isTouchingLadder:
            self.gravUpdate()

        self.rect.y += self.velocity.dy




        # Collision detection

        for floor in self.floors.sprites():
            if pygame.sprite.collide_rect(self, floor) == False:
                self.isOnGround = False

        if pygame.sprite.spritecollideany(self, self.doors) != None:
            self.doorContact = pygame.sprite.spritecollideany(self, self.doors)
            self.isTouchingDoor = True
        else:
            self.isTouchingDoor = False

        if pygame.sprite.spritecollideany(self, self.ladders) != None:
            self.isTouchingLadder = True
            if self.velocity.dy != 0 and self.isOnGround == False:
                self.ladderClimbingAnim(self)
        else:
            self.isTouchingLadder = False

        # if self.dataDrive != None:
        #     if pygame.sprite.collide_rect(self, self.dataDrive):
        #         print('Drive collected!')
        #         self.scene.hasDataDrive = False
        #         self.scene.MainMapManager.dir.UIandStatsManager.drivesCollected += 1



        if self.enemies != None:
            for enemy in self.enemies.sprites():
                if self.facingRight:
                    if self.isAttackingMelee and self.currCoolDownNum <= self.coolDownFramesMelee // 12 and pygame.sprite.collide_rect(self.forwardHB, enemy):
                        enemy.health -= 3
                        enemy.knockback += 3
                        enemy.velocity.dy = -10

                else:
                    if self.isAttackingMelee and self.currCoolDownNum <= self.coolDownFramesMelee // 12 and pygame.sprite.collide_rect(self.backwardHB, enemy):
                        enemy.health -= 3
                        enemy.knockback -= 3
                        enemy.velocity.dy = -10


        if self.iFrames != 0:
            self.iFrames -= 1




        horiz_walls_hit = pygame.sprite.spritecollide(self, self.horizWalls, False)
        for wall in horiz_walls_hit:

            if self.velocity.dy > 0.0:
                self.isOnGround = True
                self.rect.bottom = wall.rect.top
            elif self.velocity.dy < 0.0:
                self.isOnGround = False
                self.rect.top = wall.rect.bottom
                self.rect.y += 1.0



        vert_walls_hit = pygame.sprite.spritecollide(self, self.vertWalls, False)
        for wall in vert_walls_hit:

            if self.velocity.dx > 0.0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right
