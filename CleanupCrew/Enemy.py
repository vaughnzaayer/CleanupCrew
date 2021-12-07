import pygame
from SpriteSheet import SpriteSheet
from AnimationHandlerFW import AnimationHandler
from Physics import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = SpriteSheet('Assets/Alien.png')

        self.animationManager = AnimationHandler(self.sprite_sheet)

        self.trackingPlayer = None

        self.image = self.sprite_sheet.parse_sprite('Alien 0.aseprite')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()

        self.gravity = 0.25
        self.velocity = Vector2D(0.0, 0.0)

        self.vertWalls = None
        self.horizWalls = None
        self.floors = None

        self.scene = None

        self.isOnGround = False

        self.facingRight = True
        self.frameCount = 0
        self.currentFrame = 0

        self.movingAnim, self.movingAnimRev = self.animationManager.createAnim([0, 2], 15, True)

        self.patrolling = True

        self.health = 20
        self.knockback = 0




    def jump(self):
        if self.isOnGround:
            self.velocity.dy = -10


    def patrol(self):
        # Move the enemy in it's facing direction
        if self.facingRight:
            self.velocity.dx = 6
            self.facingRight = True
        else:
            self.velocity.dx = -6
            self.facingRight = False

        if self.trackingPlayer != None:
            if self.trackingPlayer.isOnGround == False:
                self.jump()


    def gravUpdate(self):
        if not self.isOnGround:
            self.velocity.dy += self.gravity


    def update(self):
        # print(str(self.rect.x) + ' ' + str(self.rect.y))
        # Updating position based on movement
        if self.isOnGround and self.knockback == 0:
            self.patrol()
        self.velocity.dx += self.knockback
        self.rect.x += self.velocity.dx
        self.knockback = 0

        if self.health <= 0:
            self.kill()

        # Updating position based on gravity
        self.gravUpdate()
        self.rect.y += self.velocity.dy

        # Animation updates

        if self.velocity.dx == 0:
            if self.facingRight:
                pass
            else:
                pass

        elif self.velocity.dx > 0:
            self.movingAnim(self)

        else:
            self.movingAnimRev(self)

        # Collision detection

        for floor in self.floors.sprites():
            if pygame.sprite.collide_rect(self, floor) == False:
                self.isOnGround = False

        for projectile in self.scene.projectiles.sprites():
            if pygame.sprite.collide_rect(self, projectile) == True:
                self.health -= 10
                projectile.kill()

        if self.trackingPlayer != None and self.scene.MainMapManager.dir != None:
            if pygame.sprite.collide_rect(self, self.trackingPlayer):
                if self.scene.MainMapManager.dir.UIandStatsManager.playerHealth > 0:
                    self.scene.MainMapManager.dir.UIandStatsManager.playerHealth -= 1
                    if self.facingRight:
                        self.trackingPlayer.velocity.dx = 5
                    else:
                        self.trackingPlayer.velocity.dx = -5
                    self.trackingPlayer.velocity.dy = -5


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
                self.facingRight = False
            else:
                self.rect.left = wall.rect.right
                self.facingRight = True
