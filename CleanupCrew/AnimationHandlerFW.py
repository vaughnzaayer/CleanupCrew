import pygame, json
from SpriteSheet import SpriteSheet


class AnimationHandler:

    def __init__(self, spriteSheet):
        self.spriteSheet = spriteSheet
        self.allFrames = []
        for frame in self.spriteSheet.data['frames']:
            frame = self.spriteSheet.parse_sprite(frame)
            # frame = pygame.transform.scale(frame, (120, 120))
            self.allFrames.append(frame)

    def createAnim(self, listOfFrames, frameTime, requiresInverse):

        frameCycle = []

        for frameNumber in listOfFrames:
            requiredFrame = self.allFrames[frameNumber]
            frameCycle.append(requiredFrame)


        if requiresInverse:

            reversedFrameCycle = []

            for frameNumber in listOfFrames:
                requiredFrame = self.allFrames[frameNumber]
                requiredFrame = pygame.transform.flip(requiredFrame, True, False)
                reversedFrameCycle.append(requiredFrame)

            def anim(Sprite):
                localFrameTime = frameTime
                # frameCycle = []
                currentFrame = Sprite.currentFrame

                # for frameNumber in listOfFrames:
                #     requiredFrame = self.allFrames[frameNumber]
                #     frameCycle.append(requiredFrame)

                if Sprite.currentFrame >= localFrameTime:
                    if Sprite.image not in frameCycle:
                        Sprite.image = frameCycle[0]
                        Sprite.currentFrame = 0
                    else:
                        if frameCycle[frameCycle.index(Sprite.image)] == frameCycle[-1]:
                            Sprite.image = frameCycle[0]
                            Sprite.currentFrame = 0
                        else:
                            Sprite.image = frameCycle[frameCycle.index(Sprite.image) + 1]
                            Sprite.currentFrame = 0
                else:
                    Sprite.currentFrame += 1

            def reversedAnim(Sprite):
                localFrameTime = frameTime
                # reversedFrameCycle = []
                currentFrame = Sprite.currentFrame

                # for frameNumber in listOfFrames:
                #     requiredFrame = self.allFrames[frameNumber]
                #     requiredFrame = pygame.transform.flip(requiredFrame, True, False)
                #     reversedFrameCycle.append(requiredFrame)

                if Sprite.currentFrame >= localFrameTime:
                    if Sprite.image not in reversedFrameCycle:
                        Sprite.image = reversedFrameCycle[0]
                        Sprite.currentFrame = 0
                    else:
                        if reversedFrameCycle[reversedFrameCycle.index(Sprite.image)] == reversedFrameCycle[-1]:
                            Sprite.image = reversedFrameCycle[0]
                            Sprite.currentFrame = 0
                        else:
                            Sprite.image = reversedFrameCycle[reversedFrameCycle.index(Sprite.image) + 1]
                            Sprite.currentFrame = 0
                else:
                    Sprite.currentFrame += 1


            return anim, reversedAnim

        else:

            def anim(Sprite):
                localFrameTime = frameTime
                # frameCycle = []
                currentFrame = Sprite.currentFrame

                # for frameNumber in listOfFrames:
                #     requiredFrame = self.allFrames[frameNumber]
                #     frameCycle.append(requiredFrame)

                if Sprite.currentFrame >= localFrameTime:
                    if Sprite.image not in frameCycle:
                        Sprite.image = frameCycle[0]
                        Sprite.currentFrame = 0
                    else:
                        if frameCycle[frameCycle.index(Sprite.image)] == frameCycle[-1]:
                            Sprite.image = frameCycle[0]
                            Sprite.currentFrame = 0
                        else:
                            Sprite.image = frameCycle[frameCycle.index(Sprite.image) + 1]
                            Sprite.currentFrame = 0
                else:
                    Sprite.currentFrame += 1

            return anim
