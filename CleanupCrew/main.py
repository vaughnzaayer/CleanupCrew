# Modules
import pygame, sys
from SceneManager import Director
from Scene import Scene
from TestScene import TestScene
from OpenScene import OpenScene
from Player import Player
from Room import Room
from Airlock import Airlock
from MainMenu import MainMenu

GREY = (115, 115, 115)
RED = (255, 0, 0)

def main():
    dir = Director()
    scene = MainMenu(dir)
    dir.changeScene(scene, None)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()
