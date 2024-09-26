# This file to run the game
import sys

import pygame
from level import Level
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption('Breath through Cold')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.win.fill('white')

            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
