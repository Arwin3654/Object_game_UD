import pygame
from settings import *






class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, clutch):
        super().__init__(clutch)
        self.image = pygame.image.load('Sprites/Wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

class door(pygame.sprite.Sprite):
    def __init__(self, pos, clutch):
        super().__init__(clutch)
        self.image = pygame.image.load('Sprites/Door.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
