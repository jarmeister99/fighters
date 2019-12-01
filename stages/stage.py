import pygame

from tiles.grass import Grass


class StageBuilder():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def load_stage(self, stage_key):
        tiles = pygame.sprite.Group()
        if stage_key == 'GRASS_PLATFORM':
            for i in range(self.width // 64 + 1):
                tiles.add(Grass(i * 64, self.height - 64, 64, 64))
        return tiles
